import re
from typing import List
from backend.speech_processing.transcribe import transcribe_audio

def detect_keywords(audio_path: str, keywords: List[str]) -> List[str]:
    """
    Detect specific keywords in the transcribed audio.
    
    Args:
        audio_path (str): Path to the audio file.
        keywords (List[str]): List of keywords to search for.
    
    Returns:
        List[str]: List of detected keywords found in the audio.
    """
    transcript = transcribe_audio(audio_path)
    if not transcript or "error" in transcript.lower():
        return [f"Error during transcription: {transcript}"]
    
    found_keywords = set()
    for keyword in keywords:
        if re.search(rf"\b{re.escape(keyword)}\b", transcript, re.IGNORECASE):
            found_keywords.add(keyword)
    
    return list(found_keywords)
