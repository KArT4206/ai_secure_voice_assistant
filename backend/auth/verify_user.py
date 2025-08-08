import json
import os
from .utils import load_model_and_verify

def verify_login(username, password, pattern):
    cred_path = f"backend/auth/model/{username}_cred.json"
    if not os.path.exists(cred_path):
        return False

    with open(cred_path, "r") as f:
        data = json.load(f)
        if data["password"] != password:
            return False

    return load_model_and_verify(username, pattern)
