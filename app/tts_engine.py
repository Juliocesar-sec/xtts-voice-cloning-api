import os
import torch
import uuid
import re
from TTS.api import TTS
from app.config import OUTPUTS_DIR, VOICES_DIR

# Correção para PyTorch 2.6+
torch.serialization.add_safe_globals(["XttsConfig"])

# Configuração focada em CPU para o Debian
device = "cpu"
tts_model = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

def clean_text_for_tts(text: str) -> str:
    """
    Limpa o texto de forma agressiva para o modelo XTTS não ler a pontuação.
    """
    # 1. Remove quebras de linha físicas e espaços duplos
    text = text.replace("\n", " ").replace("\r", " ")
    text = re.sub(r'\s+', ' ', text)
    
    # 2. REMOVE espaços antes da pontuação (Causa principal do erro "ponto")
    text = re.sub(r'\s+([.!?;,:])', r'\1', text)
    
    # 3. TRUQUE PARA XTTS: Substitui pontos finais por uma pequena pausa
    # Adicionamos um espaço duplo após a pontuação para forçar o silêncio do modelo.
    text = re.sub(r'([.!?;,:])', r'\1  ', text)
    
    # 4. Limpeza de caracteres não permitidos (mantém acentos e pontuação básica)
    text = re.sub(r'[^a-zA-Z0-9áéíóúâêôãõçÀÉÍÓÚÂÊÔÃÕÇ.!?;,:\s]', '', text)
    
    return text.strip()

def generate_audio(text: str, speaker: str = None, language: str = "pt"):
    # Limpa o texto usando a nova lógica
    cleaned_text = clean_text_for_tts(text)
    
    # Se mesmo assim ele falar "ponto", podemos testar remover o ponto final
    # e deixar apenas o espaço, mas o cleaned_text acima costuma resolver.
    
    unique_name = f"tts_{uuid.uuid4().hex}.wav"
    output_path = os.path.join(OUTPUTS_DIR, unique_name)

    speaker_wav = os.path.join(VOICES_DIR, speaker) if speaker else None

    # O XTTS v2 às vezes precisa que o texto não termine abruptamente com um ponto isolado
    tts_model.tts_to_file(
        text=cleaned_text,
        file_path=output_path,
        language=language,
        speaker_wav=speaker_wav
    )
    
    return output_path
