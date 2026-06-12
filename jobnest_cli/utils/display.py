def show_users(users):
    if not users:
        print("No users found. Try add-user to create one.")
        return
    print("Users:")
    for u in users:
        skills = ", ".join(getattr(u, "skills", [])) if getattr(u, "skills", None) else "-"
        projects_count = len(getattr(u, "projects", []))
        print(f" - {getattr(u, 'id', '?')} | {u.name} | {u.email} | skills: {skills} | projects: {projects_count}")


def show_projects(user):
    if not getattr(user, "projects", None):
        print(f"{user.name} has no projects yet.")
        return
    print(f"Projects for {user.name}:")
    for p in user.projects:
        done = len([t for t in p.tasks if t.status == "done"]) if getattr(p, "tasks", None) else 0
        total = len(getattr(p, "tasks", []))
        tasks_part = f"{done}/{total}" if total else "no tasks"
        due = p.due_date or "(no due)"
        print(f" - {p.id}: {p.title} | due: {due} | tasks: {tasks_part}")