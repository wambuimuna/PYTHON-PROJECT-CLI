import argparse
from jobnest_cli.models.user import User
from jobnest_cli.utils.file_io import load_users, save_users
from jobnest_cli.utils.display import show_users, show_projects

def main():
    parser = argparse.ArgumentParser(description="JobNest CLI - Project Management")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Command: add-user
    p_add_user = subparsers.add_parser("add-user", help="Register a new user")
    p_add_user.add_argument("--name", required=True, help="User's full name")
    p_add_user.add_argument("--email", required=True, help="User's email address")
    # Kept as a simple string argument instead of nargs or custom types
    p_add_user.add_argument("--skills", default="", help="Comma-separated skills")
    p_add_user.add_argument("--bio", default="", help="Short biography")

    args = parser.parse_args()
    users = load_users()

    if args.command == "add-user":
        # Manual string splitting directly in the command handler
        skills_list = []
        if args.skills:
            skills_list = [s.strip() for s in args.skills.split(",")]
        
        new_user = User(name=args.name, email=args.email, skills=skills_list, bio=args.bio)
        users.append(new_user)
        save_users(users)
        print(f"User {args.name} added successfully!")
        
    elif args.command == "view-users":
        show_users(users)

if __name__ == "__main__":
    main()