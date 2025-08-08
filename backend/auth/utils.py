import os
import joblib
import numpy as np
from hmmlearn import hmm

def extract_features(pattern: str):
    return np.array([[int(char)] for char in pattern if char.isdigit()])

def train_model(username: str, pattern: str):
    model = hmm.GaussianHMM(n_components=4, covariance_type="diag", n_iter=100)
    features = extract_features(pattern)
    model.fit(features)

    joblib.dump(model, f"backend/auth/model/{username}_model.pkl")

def load_model_and_verify(username: str, pattern: str) -> bool:
    try:
        model = joblib.load(f"backend/auth/model/{username}_model.pkl")
        test_features = extract_features(pattern)
        score = model.score(test_features)
        return score > -50  # basic threshold
    except Exception:
        return False
