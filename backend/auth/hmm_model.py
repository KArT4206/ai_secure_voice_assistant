import joblib
import os
from hmmlearn import hmm
import numpy as np

def train_and_save_hmm(username, pattern_list):
    X = np.array([float(i) for i in pattern_list]).reshape(-1, 1)
    model = hmm.GaussianHMM(n_components=3, covariance_type="diag", n_iter=100)
    model.fit(X)
    joblib.dump(model, f"users_data/{username}_hmm.pkl")

def verify_hmm_pattern(username, test_pattern):
    model_path = f"users_data/{username}_hmm.pkl"
    if not os.path.exists(model_path):
        return False

    model = joblib.load(model_path)
    X_test = np.array([float(i) for i in test_pattern]).reshape(-1, 1)
    try:
        score = model.score(X_test)
        return score > -100  # Threshold can be tuned
    except:
        return False
