import os
import torch
import uuid
import re  # IMPORTANTE: Adicionamos o Regex para limpeza
from TTS.api import TTS
from app.config import OUTPUTS_DIR, VOICES_DIR

# Correção para PyTorch 2.6+
torch.serialization.add_safe_globals(["XttsConfig"])

# Configuração focada em CPU para o Debian
device = "cpu"
tts_model = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

def clean_text_for_tts(text: str) -> str:
    """
    Limpa o texto para evitar que o modelo leia pontuações em voz alta.
    """
    # 1. Remove espaços extras e quebras de linha que confundem o motor
    text = text.replace("\n", " ").replace("\r", " ")
    text = re.sub(r'\s+', ' ', text)
    
    # 2. Garante que não haja espaço ANTES da pontuação (ex: "casa ." -> "casa.")
    # Isso é o que geralmente faz ele ler a palavra "ponto"
    text = re.sub(r'\s+([.!?;,])', r'\1', text)
    
    # 3. Garante que haja um espaço DEPOIS da pontuação para o modelo 'respirar'
    text = re.sub(r'([.!?;,])(?=[^\s])', r'\1 ', text)
    
    return text.strip()

def generate_audio(text: str, speaker: str = None, language: str = "pt"):
    # Limpa o texto antes de enviar para o modelo
    cleaned_text = clean_text_for_tts(text)
    
    # Gera um nome aleatório para não sobrescrever arquivos
    unique_name = f"tts_{uuid.uuid4().hex}.wav"
    output_path = os.path.join(OUTPUTS_DIR, unique_name)

    # Define o caminho da voz de referência (ex: paulo.wav)
    speaker_wav = os.path.join(VOICES_DIR, speaker) if speaker else None

    # Processa o texto limpo
    tts_model.tts_to_file(
        text=cleaned_text,
        file_path=output_path,
        language=language,
        speaker_wav=speaker_wav
    )
    
    return output_path
