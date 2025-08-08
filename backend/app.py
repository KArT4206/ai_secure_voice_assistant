from fastapi import FastAPI, UploadFile, File, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
import os

from backend.speech_processing.transcribe import transcribe_audio
from backend.auth.verify_user import verify_login
from backend.auth.train_auth_model import register_user
from backend.nlp_modules.sentiment_analysis import analyze_sentiment
from ai_brain.intent_classifier import classify_intent
from backend.nlp_modules.summarizer import summarize_text

app = FastAPI(title="AI Secure Voice Assistant")
app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
def serve_index():
    return FileResponse("frontend/index.html")

@app.get("/login/")
def serve_login():
    return FileResponse("frontend/login.html")

# --- AI VOICE + NLP ---

@app.post("/transcribe/")
async def transcribe_audio_endpoint(file: UploadFile = File(...)):
    audio_data = await file.read()
    text = transcribe_audio(audio_data)
    return {"transcription": text}

@app.post("/nlp/sentiment/")
async def sentiment_analysis(text: str = Form(...)):
    result = analyze_sentiment(text)
    return {"sentiment": result}

@app.post("/ai/intent/")
async def intent_classification(text: str = Form(...)):
    intent = classify_intent(text)
    return {"intent": intent}

@app.post("/nlp/summarize/")
async def summarization(text: str = Form(...)):
    result = summarize_text(text)
    return {"summary": result}

# --- AUTHENTICATION ---

@app.post("/register/")
async def register(username: str = Form(...), password: str = Form(...), keystroke_pattern: str = Form(...)):
    success = register_user(username, password, keystroke_pattern)
    if success:
        return {"status": "registered"}
    return JSONResponse(status_code=400, content={"status": "registration_failed"})

@app.post("/login/")
async def login(username: str = Form(...), password: str = Form(...), keystroke_pattern: str = Form(...)):
    verified = verify_login(username, password, keystroke_pattern)
    return {"authenticated": verified}
