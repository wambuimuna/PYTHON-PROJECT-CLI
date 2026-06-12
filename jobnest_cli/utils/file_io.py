import json, os
from models.user import User

DATA_DIR = "data"
USERS_FILE = os.path.join(DATA_DIR, "users.json")

def load_users() -> list:
    try:
        with open(USERS_FILE, "r") as f:
            return [User.from_dict(u) for u in json.load(f)]
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_users(users: list):
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(USERS_FILE, "w") as f:
        json.dump([u.to_dict() for u in users], f, indent=2)