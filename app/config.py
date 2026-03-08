# Pega a raiz do projeto independente de onde o script é chamado
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

OUTPUTS_DIR = os.path.join(BASE_DIR, "outputs")
VOICES_DIR = os.path.join(BASE_DIR, "voices")
MODELS_DIR = os.path.join(BASE_DIR, "models")

# Garante a criação das pastas ao iniciar a API
os.makedirs(OUTPUTS_DIR, exist_ok=True)
os.makedirs(VOICES_DIR, exist_ok=True)
os.makedirs(MODELS_DIR, exist_ok=True)
