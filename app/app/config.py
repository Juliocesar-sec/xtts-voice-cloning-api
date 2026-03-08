import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUTS_DIR = os.path.join(BASE_DIR, "outputs")
VOICES_DIR = os.path.join(BASE_DIR, "voices")

os.makedirs(OUTPUTS_DIR, exist_ok=True)
os.makedirs(VOICES_DIR, exist_ok=True)

### Define diretórios de saída e vozes e garante que existam.
