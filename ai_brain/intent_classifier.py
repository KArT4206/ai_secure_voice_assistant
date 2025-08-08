import os
import joblib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Paths
MODEL_PATH = "models/intent_classifier.pt"
VECTORIZER_PATH = "models/intent_vectorizer.pkl"

# Load or initialize
if os.path.exists(MODEL_PATH) and os.path.exists(VECTORIZER_PATH):
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
else:
    # Dummy training if not found
    intents = ["play music", "set alarm", "get weather", "tell joke", "shutdown system"]
    labels = ["music", "alarm", "weather", "joke", "shutdown"]

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(intents)

    model = LogisticRegression()
    model.fit(X, labels)

    # Save them
    joblib.dump(model, MODEL_PATH)
    joblib.dump(vectorizer, VECTORIZER_PATH)

def classify_intent(text: str) -> str:
    try:
        X = vectorizer.transform([text])
        prediction = model.predict(X)
        return prediction[0]
    except Exception as e:
        return f"Intent classification failed: {str(e)}"
