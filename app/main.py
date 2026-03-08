from fastapi import FastAPI
from app.routes import tts

app = FastAPI(title="TTS API")

app.include_router(tts.router, prefix="/v1")

### Responsável por inicializar a API e incluir as rotas do TTS.
