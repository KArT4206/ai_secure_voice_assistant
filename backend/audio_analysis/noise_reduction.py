import noisereduce as nr
import numpy as np
import soundfile as sf
import librosa

def reduce_noise(audio_path: str, output_path: str = None) -> str:
    """
    Applies noise reduction to the given audio file.
    
    Args:
        audio_path (str): Path to input audio file.
        output_path (str): Optional path to save cleaned audio.
    
    Returns:
        str: Path to the noise-reduced audio file.
    """
    try:
        y, sr = librosa.load(audio_path, sr=None)
        
        # Estimate noise from first 0.5 seconds (can be tuned)
        noise_sample = y[:int(0.5 * sr)]
        reduced_noise = nr.reduce_noise(y=y, sr=sr, y_noise=noise_sample, prop_decrease=1.0)

        if output_path is None:
            output_path = audio_path.replace(".wav", "_cleaned.wav")

        sf.write(output_path, reduced_noise, sr)
        return output_path
    except Exception as e:
        return f"Noise reduction failed: {str(e)}"
