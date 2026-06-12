# JobNest (student version)

A tiny, student-friendly CLI for tracking users and their projects. The implementation is intentionally simple and stores data as JSON in `data/users.json`.

Current scope
-------------
- Commands available today:
	- `add-user` — register a new user/profile
	- `view-users` — display saved users
	- `add-project` — add a project to a user (requires `--user-id`)
	- `view-projects` — list projects for a user (`--user-id`)
	- `add-task` — add a task to a project (`--user-id` and `--project-id`)
	- `view-tasks` — show tasks for a project or user
	- `complete-task` — mark a task done (`--user-id --project-id --task-id`)

Project layout
--------------
- `main.py` — CLI entrypoint (argparse)
- `models/` — `Person`, `User`, `Project`, `Task` classes
- `utils/file_io.py` — JSON persistence (`data/users.json`)
- `utils/display.py` — simple `print` helpers
- `data/` — stores `users.json` (created as needed)
- `tests/` — minimal tests and helper functions

Getting started
---------------

1. (Optional) Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. (Optional) Install dev/test tools:

```bash
pip install -r requirements.txt
```

How to run the CLI
-------------------

Recommended (module invocation):

```bash
python3 -m jobnest_cli.main add-user --name "Alice" --email alice@example.com --skills "python,tests" --bio "student"
```

View saved users:

```bash
python3 -m jobnest_cli.main view-users
```

Add a project for a user (requires `--user-id`):

```bash
python3 -m jobnest_cli.main add-project --user-id 1 --title "Term Project" --description "CLI work" --due "2026-06-30"
```

View a user's projects:

```bash
python3 -m jobnest_cli.main view-projects --user-id 1
```

Add a task to a project:

```bash
python3 -m jobnest_cli.main add-task --user-id 1 --project-id 1 --title "Write tests" --assigned-to "Alice"
```

View tasks (project-specific):

```bash
python3 -m jobnest_cli.main view-tasks --user-id 1 --project-id 1
```

Mark a task done:

```bash
python3 -m jobnest_cli.main complete-task --user-id 1 --project-id 1 --task-id 1
```

Direct script invocation (alternative):

```bash
PYTHONPATH=. python3 jobnest_cli/main.py add-user --name "Alice" --email alice@example.com --skills "python,tests" --bio "student"
``

Run the test suite (from the repo root):

```bash
pytest -q
```


License
-------

Provided as-is for learning and demonstration purposes.
