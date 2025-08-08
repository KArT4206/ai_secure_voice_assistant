import os
from auth.hmm_model import verify_hmm_pattern
from users.storage import load_user_credentials

def login_user(username, password, pattern):
    if not os.path.exists(f"users_data/{username}.json"):
        return {"status": "fail", "reason": "User not found"}

    stored_password = load_user_credentials(username)
    if stored_password != password:
        return {"status": "fail", "reason": "Invalid password"}

    pattern_list = pattern.split(",")
    is_genuine = verify_hmm_pattern(username, pattern_list)

    if is_genuine:
        return {"status": "success", "message": "Login successful"}
    else:
        return {"status": "fail", "reason": "Keystroke pattern mismatch"}
