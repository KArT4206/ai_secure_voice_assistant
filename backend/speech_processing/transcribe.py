import io
import whisper
from pydub import AudioSegment

# Load Whisper model once
model = whisper.load_model("base")

def transcribe_audio(audio_bytes: bytes) -> str:
    try:
        # Convert to WAV (required by Whisper)
        audio = AudioSegment.from_file(io.BytesIO(audio_bytes))
        wav_io = io.BytesIO()
        audio.export(wav_io, format="wav")
        wav_io.seek(0)

        # Transcribe using Whisper
        result = model.transcribe(wav_io)
        return result["text"]
    except Exception as e:
        return f"Transcription Error: {str(e)}"
