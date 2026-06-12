# JobNest (student version)

 A tiny CLI app to track people, their projects, and tasks — implemented in a simple, student-friendly style.

 This repository contains a small command-line tool called `jobnest` that stores users, projects, and tasks in JSON files under the `data/` directory. The code is intentionally simple and easy to read so a student can understand and modify it.

 **Features**
- Add and list users (profiles)
- Add projects for users and list projects
- Add tasks to projects and mark tasks complete
- Search users by skill

 **Project layout**

- `main.py` — CLI entrypoint (simple argparse-based commands)
- `models/` — small classes for `Person`, `User`, `Project`, `Task`
- `utils/file_io.py` — read/write JSON data (`data/users.json`)
- `utils/display.py` — simple `print`-based output helpers
- `data/` — where `users.json` is stored (created at runtime)
- `tests/` — basic tests demonstrating helper functions

 Getting started
 ---------------

 1. Create and activate a virtualenv (recommended):

 ```bash
 python3 -m venv .venv
 source .venv/bin/activate
 ```

 2. Install dev/test tools (optional):

 ```bash
 pip install -r requirements.txt
 pip install pytest
 ```

 Run the CLI
 ----------

 The CLI is driven by `main.py`. Example usage:

- Add a user:

 ```bash
 python3 main.py add-user --name "Alice" --email alice@example.com --skills "python,tests" --bio "student"
 ```

- List users:

 ```bash
 python3 main.py list-users
 ```

- Add a project to a user:

 ```bash
 python3 main.py add-project --user "Alice" --title "Homework" --description "Do exercises" --due-date "2026-06-30"
 ```

- List a user's projects:

 ```bash
 python3 main.py list-projects --user "Alice"
 ```

- Add a task to a project:

 ```bash
 python3 main.py add-task --user "Alice" --project "Homework" --title "Problem 1" --assigned-to "Alice"
 ```

- Mark a task complete:

 ```bash
 python3 main.py complete-task --user "Alice" --project "Homework" --task "Problem 1"
 ```

- Search users by skill:

 ```bash
 python3 main.py search-users --skill python
 ```

 Data storage
 ------------

 User and project data is stored in `data/users.json`. The app will create the `data/` folder and file when you first save something.

 Testing
 -------

 If you have `pytest` installed, run:

 ```bash
 pytest -q
 ```

 Notes for students
 ------------------

- The implementation is intentionally simple: public attributes on models, plain `print` output, and straightforward JSON persistence.
- Feel free to refactor: add better error handling, CLI prompts, or replace JSON with a small database.

 License
 -------

 This project is provided as-is for learning and demonstration purposes.# jobnest_cli

A tiny CLI scaffold for managing people, users, projects and tasks.

Usage:

- `python main.py list-users` — list users from the simple JSON database.

Run tests:

```bash
pip install -r requirements.txt
pytest -q
```
