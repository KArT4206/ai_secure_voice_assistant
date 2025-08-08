import json
import os
from statistics import mean

USER_FILE = "backend/data/users.json"

if not os.path.exists(USER_FILE):
    with open(USER_FILE, "w") as f:
        json.dump({}, f)

def load_users():
    with open(USER_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=4)

def register_user(username, password, keystrokes):
    users = load_users()
    if username in users:
        return {"status": "fail", "msg": "Username already exists"}
    users[username] = {
        "password": password,
        "keystrokes": keystrokes
    }
    save_users(users)
    return {"status": "success", "msg": "Registered"}

def verify_user(username, password, input_keystrokes):
    users = load_users()
    if username not in users:
        return {"status": "fail", "msg": "User not found"}
    if users[username]["password"] != password:
        return {"status": "fail", "msg": "Incorrect password"}
    stored_keystrokes = users[username]["keystrokes"]
    score = mean([abs(a - b) for a, b in zip(stored_keystrokes, input_keystrokes)])
    if score < 80:  # adjust threshold as needed
        return {"status": "success", "msg": "Login successful"}
    else:
        return {"status": "fail", "msg": "Keystroke authentication failed"}
