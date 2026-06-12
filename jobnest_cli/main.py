import argparse
from typing import Optional

from jobnest_cli.models.user import User
from jobnest_cli.models.project import Project
from jobnest_cli.models.task import Task
from jobnest_cli.utils.file_io import load_users, save_users
from jobnest_cli.utils.display import show_users, show_projects


def find_user(users: list, user_id: int) -> Optional[User]:
    for u in users:
        if getattr(u, "id", None) == user_id:
            return u
    return None


def main():
    parser = argparse.ArgumentParser(description="JobNest CLI - Project Management")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    p_add_user = subparsers.add_parser("add-user", help="Register a new user")
    p_add_user.add_argument("--name", required=True, help="User's full name")
    p_add_user.add_argument("--email", required=True, help="User's email address")
    p_add_user.add_argument("--skills", default="", help="Comma-separated skills")
    p_add_user.add_argument("--bio", default="", help="Short biography")

    subparsers.add_parser("view-users", help="Show all saved users")

    p_add_project = subparsers.add_parser("add-project", help="Add a project for a user")
    p_add_project.add_argument("--user-id", type=int, required=True, help="Owner user id")
    p_add_project.add_argument("--title", required=True, help="Project title")
    p_add_project.add_argument("--description", default="", help="Short description")
    p_add_project.add_argument("--due", default="", help="Due date (free text)")

    p_view_projects = subparsers.add_parser("view-projects", help="List projects for a user")
    p_view_projects.add_argument("--user-id", type=int, required=True, help="User id")

    p_add_task = subparsers.add_parser("add-task", help="Add a task to a user's project")
    p_add_task.add_argument("--user-id", type=int, required=True, help="Owner user id")
    p_add_task.add_argument("--project-id", type=int, required=True, help="Project id")
    p_add_task.add_argument("--title", required=True, help="Task title")
    p_add_task.add_argument("--assigned-to", default="", help="Person assigned to task (name)")

    p_view_tasks = subparsers.add_parser("view-tasks", help="Show tasks for a project or user")
    p_view_tasks.add_argument("--user-id", type=int, required=True, help="User id")
    p_view_tasks.add_argument("--project-id", type=int, help="Project id (optional)")

    p_complete = subparsers.add_parser("complete-task", help="Mark a task done")
    p_complete.add_argument("--user-id", type=int, required=True, help="User id")
    p_complete.add_argument("--project-id", type=int, required=True, help="Project id")
    p_complete.add_argument("--task-id", type=int, required=True, help="Task id")

    args = parser.parse_args()
    users = load_users()

    if args.command == "add-user":
        skills_list = [s.strip() for s in args.skills.split(",") if s.strip()] if args.skills else []
        new_user = User(name=args.name, email=args.email, skills=skills_list, bio=args.bio)
        users.append(new_user)
        save_users(users)
        print(f"User {args.name} added successfully!")

    elif args.command == "view-users":
        show_users(users)

    elif args.command == "add-project":
        user = find_user(users, args.user_id)
        if not user:
            print(f"User id {args.user_id} not found")
            return
        proj = Project(title=args.title, description=args.description, due_date=args.due)
        user.add_project(proj)
        save_users(users)
        print(f"Project '{args.title}' added to {user.name} (id {user.id})")

    elif args.command == "view-projects":
        user = find_user(users, args.user_id)
        if not user:
            print(f"User id {args.user_id} not found")
            return
        show_projects(user)

    elif args.command == "add-task":
        user = find_user(users, args.user_id)
        if not user:
            print(f"User id {args.user_id} not found")
            return
        proj = next((p for p in user.projects if getattr(p, "id", None) == args.project_id), None)
        if not proj:
            print(f"Project id {args.project_id} not found for user {user.name}")
            return
        task = Task(title=args.title, assigned_to=args.assigned_to or "")
        proj.add_task(task)
        save_users(users)
        print(f"Task '{args.title}' added to project '{proj.title}'")

    elif args.command == "view-tasks":
        user = find_user(users, args.user_id)
        if not user:
            print(f"User id {args.user_id} not found")
            return
        if args.project_id:
            proj = next((p for p in user.projects if getattr(p, "id", None) == args.project_id), None)
            if not proj:
                print(f"Project id {args.project_id} not found for user {user.name}")
                return
            print(f"Tasks for project '{proj.title}':")
            for t in proj.tasks:
                print(f" - {t}")
        else:
            print(f"All tasks for {user.name}:")
            for p in user.projects:
                for t in p.tasks:
                    print(f" - ({p.id}) {p.title}: {t}")

    elif args.command == "complete-task":
        user = find_user(users, args.user_id)
        if not user:
            print(f"User id {args.user_id} not found")
            return
        proj = next((p for p in user.projects if getattr(p, "id", None) == args.project_id), None)
        if not proj:
            print(f"Project id {args.project_id} not found for user {user.name}")
            return
        task = next((t for t in proj.tasks if getattr(t, "id", None) == args.task_id), None)
        if not task:
            print(f"Task id {args.task_id} not found in project {proj.title}")
            return
        task.complete()
        save_users(users)
        print(f"Task {task.id} marked as done")


if __name__ == "__main__":
    main()