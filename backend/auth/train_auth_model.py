import os
import json
from .utils import train_model

def register_user(username, password, keystroke_data):
    user_dir = "backend/auth/model"
    os.makedirs(user_dir, exist_ok=True)
    
    # Save user credentials
    cred_path = os.path.join(user_dir, f"{username}_cred.json")
    if os.path.exists(cred_path):
        return False  # user exists

    with open(cred_path, "w") as f:
        json.dump({"username": username, "password": password}, f)

    # Train and save keystroke model
    train_model(username, keystroke_data)
    return True
