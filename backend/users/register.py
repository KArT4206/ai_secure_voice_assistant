import os
import json
from auth.hmm_model import train_and_save_hmm
from users.storage import save_user_credentials

def register_user(username, password, pattern):
    if not os.path.exists("users_data"):
        os.makedirs("users_data")

    user_file = f"users_data/{username}.json"
    if os.path.exists(user_file):
        return {"status": "fail", "reason": "Username already exists"}

    # Save username and password
    save_user_credentials(username, password)

    # Train and save keystroke model
    pattern_list = pattern.split(",")
    train_and_save_hmm(username, pattern_list)

    return {"status": "success", "message": "User registered"}
