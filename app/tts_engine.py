import os
import torch
import uuid
from TTS.api import TTS
from app.config import OUTPUTS_DIR, VOICES_DIR

# Correção para PyTorch 2.6+
torch.serialization.add_safe_globals(["XttsConfig"])

# Configuração focada em CPU para o Debian
device = "cpu"
tts_model = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

def generate_audio(text: str, speaker: str = None, language: str = "pt"):
    # Gera um nome aleatório para não sobrescrever arquivos
    unique_name = f"tts_{uuid.uuid4().hex}.wav"
    output_path = os.path.join(OUTPUTS_DIR, unique_name)

    speaker_wav = os.path.join(VOICES_DIR, speaker) if speaker else None

    tts_model.tts_to_file(
        text=text,
        file_path=output_path,
        language=language,
        speaker_wav=speaker_wav
    )
    return output_path
