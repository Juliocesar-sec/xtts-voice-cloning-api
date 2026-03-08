import os
import torch
from TTS.api import TTS
from TTS.tts.configs.xtts_config import XttsConfig

# Corrige erro do PyTorch 2.6+
torch.serialization.add_safe_globals([XttsConfig])

# Carrega modelo XTTS
tts_model = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

# garante que pasta de saída existe
os.makedirs("outputs", exist_ok=True)

def generate_audio(text: str, speaker: str = None, language: str = "pt"):

    output_path = "outputs/output.wav"

    if speaker:
        speaker_wav = f"voices/{speaker}.wav"
    else:
        speaker_wav = None

    tts_model.tts_to_file(
        text=text,
        file_path=output_path,
        language=language,
        speaker_wav=speaker_wav
    )

    return output_path, 22050
