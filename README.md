# AI Secure Voice Assistant (source)

Private source for the voice assistant with keystroke-dynamics login. Public write-up with screenshots and explanation: `ai_secure_voice_assistant`.

## Layout
| Path | Purpose |
|---|---|
| `backend/app.py` | FastAPI app: `/`, `/login/` (pages), `POST /transcribe/`, `/nlp/sentiment/`, `/nlp/summarize/`, `/ai/intent/`, `/register/`, `/login/`. |
| `backend/speech_processing/transcribe.py` | Whisper `base` speech-to-text (pydub converts any upload to WAV). |
| `backend/nlp_modules/` | `sentiment_analysis.py` (TextBlob polarity), `summarizer.py` (DistilBART). |
| `ai_brain/intent_classifier.py` | TF-IDF + logistic regression intent model (`models/intent_*.pkl/.pt`); falls back to a 5-intent dummy model. |
| `backend/auth/` | `train_auth_model.py` (register, trains a Gaussian HMM), `verify_user.py` and `utils.py` (score a typed pattern), `hmm_model.py`. |
| `backend/audio_analysis/` | Emotion, keyword spotting, noise reduction, diarization and voice-cloning helpers (not wired into the API yet). |
| `frontend/` | `index.html`, `login.html`, `script.js`, `style.css`, plus Vue components (`src/`) for a future UI. |
| `run.sh` | Convenience launcher for backend and Vue front end. |

## Run
```bash
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt          # heavy: whisper, torch, transformers, speechbrain, TTS
brew install ffmpeg                      # needed by pydub / whisper
uvicorn backend.app:app --reload         # run from the repo root; open http://127.0.0.1:8000
```

## Notes and known gaps
- `frontend/script.js` calls `/auth/keystroke/` and `/set_language/`, which `backend/app.py` does not define yet.
- Credentials are saved as plain JSON in `backend/auth/model/<user>_cred.json`; hash passwords (bcrypt/argon2) before real use.
- The HMM thresholds (`score > -50`) are simple and were not tuned; the HMM library warns when a pattern has fewer samples than model parameters.
- Pre-trained models live in `models/`; compiled `__pycache__` files are no longer tracked.

## Screenshots
![Dashboard](docs/images/dashboard.png)
![Module demo](docs/images/module-demo.png)
