import whisperx
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"

def diarize_speakers(audio_path: str, model_size="large"):
    """
    Transcribes and segments audio based on speaker identity using WhisperX.
    
    Args:
        audio_path (str): Path to the audio file (.wav or .mp3).
        model_size (str): Whisper model size (tiny, base, small, medium, large).
    
    Returns:
        list: A list of dicts with start/end time, speaker, and transcribed text.
    """
    try:
        # Load whisper model with diarization support
        model = whisperx.load_model(model_size, device)

        # Transcribe and align
        result = model.transcribe(audio_path, diarize=True)

        segments = []
        for segment in result["segments"]:
            segments.append({
                "start": segment["start"],
                "end": segment["end"],
                "speaker": segment.get("speaker", "Unknown"),
                "text": segment["text"]
            })
        return segments

    except Exception as e:
        return [{"error": f"Speaker diarization failed: {str(e)}"}]
