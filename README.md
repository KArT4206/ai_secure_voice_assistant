
# AI Secure Voice Assistant with Keystroke Dynamics Authentication

## Overview
This project is an **AI-powered voice assistant** with integrated **Keystroke Dynamics Authentication** for secure login and registration. It combines advanced NLP, speech recognition, sentiment analysis, intent classification, and summarization, all while ensuring security through keystroke-based biometric verification.

## Features
- **User Registration with Keystroke Biometrics**
  - Capture username, password, and keystroke patterns during registration.
- **User Login with Keystroke Verification**
  - Authenticate users based on username, password, and typing rhythm.
- **Speech-to-Text Transcription**
  - Convert voice input into text.
- **Sentiment Analysis**
  - Determine the sentiment (positive, negative, neutral) of the input text.
- **Intent Classification**
  - Identify the purpose of the user's query.
- **Text Summarization**
  - Summarize long pieces of text into concise versions.
- **Language Setting**
  - Switch between supported languages for AI processing.

## Project Structure
```
project/
│
├── backend/
│   ├── auth/                # Keystroke authentication logic
│   ├── nlp_modules/         # NLP-related modules
│   ├── speech_processing/   # Speech-to-text conversion
│   └── ...
│
├── frontend/
│   ├── index.html           # Main interface
│   ├── login.html           # Login page
│   ├── register.html        # Registration page
│   └── assets/              # CSS, JS, images
│
├── app.py                   # Main FastAPI application
└── requirements.txt         # Python dependencies
```

## Installation
1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the FastAPI server**
```bash
uvicorn app:app --reload
```

5. **Open the application**
```
Visit http://127.0.0.1:8000 in your browser.
```

## How It Works
1. **Registration**: Users enter their username and password, and their typing rhythm is recorded and stored securely.
2. **Login**: The system verifies the username, password, and the keystroke pattern before granting access.
3. **Voice Assistant**: Once logged in, users can:
   - Speak to the assistant for transcription.
   - Analyze the sentiment of text.
   - Classify the intent of queries.
   - Summarize lengthy text.
   - Change processing language.

## Requirements
- Python 3.8+
- FastAPI
- Uvicorn
- Dependencies listed in `requirements.txt`

## Security Notes
- Keystroke data is stored securely and never shared.
- Passwords should be hashed before storage.

## Developed by
Karthik B
Sahana 
Priyanka 

