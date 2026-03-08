from .task_queue import executor
from .tts_engine import generate_audio

def process_text(text, speaker=None):
    future = executor.submit(generate_audio, text, speaker)
    return future
