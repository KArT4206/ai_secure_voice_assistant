import json
import os

def save_user_credentials(username, password):
    data = {"username": username, "password": password}
    with open(f"users_data/{username}.json", "w") as f:
        json.dump(data, f)

def load_user_credentials(username):
    with open(f"users_data/{username}.json", "r") as f:
        data = json.load(f)
    return data["password"]
