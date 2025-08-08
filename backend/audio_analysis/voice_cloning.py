from TTS.api import TTS

# Load a multispeaker TTS model
tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=False, gpu=False)

def clone_voice(text: str, reference_wav: str, output_path: str = "cloned_output.wav"):
    """
    Clones voice based on a reference audio and synthesizes the given text in that voice.

    Args:
        text (str): Text to synthesize.
        reference_wav (str): Path to speaker's reference WAV file.
        output_path (str): Output file to save synthesized audio.
    Returns:
        str: Output path or error message.
    """
    try:
        tts.tts_to_file(text=text, speaker_wav=reference_wav, file_path=output_path)
        return output_path
    except Exception as e:
        return f"Voice cloning failed: {str(e)}"
