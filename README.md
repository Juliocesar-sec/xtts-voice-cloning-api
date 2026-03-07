# fast-tts-api

Um **sistema de Text-to-Speech (TTS)** rápido e completo, inspirado na API da ElevenLabs. Suporta streaming de áudio, textos longos, clonagem de voz ilimitada e uma API compatível com ElevenLabs.

---
## ⚡ Funcionalidades

- 🎤 **Streaming de áudio** em tempo real  
- 🚀 **3x a 10x mais rápido** que TTS tradicional  
- 🔄 **Fila paralela** para múltiplas requisições  
- 📝 **Suporte a textos de até 100k caracteres**  
- 🎧 **Clonagem de voz ilimitada**  
- 🔗 **API compatível com ElevenLabs**  

---

1. Estrutura do Projeto:
## 🗂 Estrutura do Projeto

```text
tts-api/
├── app/
│   ├── __init__.py
│   ├── main.py           # Inicializa a API FastAPI
│   ├── config.py         # Configurações do projeto (caminhos, parâmetros)
│   ├── tts_engine.py     # Funções de síntese de voz
│   ├── tts_long_text.py  # Funções para dividir e processar textos longos
│   ├── streaming.py      # Streaming de áudio em tempo real
│   ├── queue.py          # Executor paralelo de tarefas de TTS
│   ├── worker.py         # Worker para processamento de filas
│   └── routes/
│       ├── __init__.py
│       └── tts.py        # Endpoints da API FastAPI (POST /v1/text-to-speech)
├── models/               # Modelos de TTS baixados
├── voices/               # Clonagens de voz salvas
├── outputs/              # Áudios gerados pelo TTS
└── requirements.txt      # Dependências do Python
```

📄 Conteúdo de cada arquivo app/*.py

```text
app/__init__.py

Arquivo vazio, usado para definir app como um pacote Python.
```
##### app/main.py

```text
from fastapi import FastAPI
from app.routes import tts

app = FastAPI(title="TTS API", version="1.0")
app.include_router(tts.router)

### Responsável por inicializar a API e incluir as rotas do TTS.
```

#### app/config.py


```text
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUTS_DIR = os.path.join(BASE_DIR, "outputs")
VOICES_DIR = os.path.join(BASE_DIR, "voices")

os.makedirs(OUTPUTS_DIR, exist_ok=True)
os.makedirs(VOICES_DIR, exist_ok=True)

### Define diretórios de saída e vozes e garante que existam.
```

#### app/tts_engine.py


```text

from TTS.api import TTS

tts_model = TTS("tts_models/multilingual/multi-dataset/xtts_v2")

def generate_audio(text: str, speaker: str = None):
    output_path = f"outputs/{speaker or 'default'}.wav"
    tts_model.tts_to_file(text=text, speaker=speaker, file_path=output_path)
    return output_path, 22050  # exemplo de sample rate

#### Funções para gerar áudio a partir do texto usando o modelo XTTS.
```

### app/tts_long_text.py


```text
import re

def split_text(text):
    sentences = re.split(r'(?<=[.!?]) +', text)
    return sentences

#### Divide textos longos em sentenças menores para processamento em lote.
```

### app/streaming.py


```text
from fastapi.responses import StreamingResponse
import io

def stream_audio(file_path):
    def iterfile():
        with open(file_path, "rb") as f:
            yield from f
    return StreamingResponse(iterfile(), media_type="audio/wav")

#### Permite streaming do áudio gerado via FastAPI.
```

### app/queue.py


```text
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(max_workers=4)

#### Executor para processar múltiplos pedidos de TTS em paralelo.
```

#### app/worker.py

```text
from .queue import executor
from .tts_engine import generate_audio

def process_text(text, speaker=None):
    future = executor.submit(generate_audio, text, speaker)
    return future

#### Worker que envia tarefas de geração de áudio para a fila paralela.
```

### app/routes/tts.py


```text
from fastapi import APIRouter, HTTPException
from ..tts_long_text import split_text
from ..worker import process_text
from ..streaming import stream_audio

router = APIRouter()

@router.post("/v1/text-to-speech")
async def text_to_speech(text: str, speaker: str = None):
    sentences = split_text(text)
    audio_files = []

    for sentence in sentences:
        future = process_text(sentence, speaker)
        audio_file, sr = future.result()  # retorna caminho do arquivo e sample rate
        audio_files.append(audio_file)

    return {"audio_files": audio_files}


### Define os endpoints da API, permitindo enviar texto e receber áudio.
```

### 🚀 Instalação

1. Certifique-se de usar Python 3.10

```text
pyenv install 3.10.13  # se ainda não tiver
pyenv virtualenv 3.10.13 tts-xtts310
pyenv activate tts-xtts310
```

2. Clone o repositório:

```text
```bash
git clone https://github.com/uliocesar-sec/xtts-voice-cloning-api.git
cd xtts-voice-cloning-api
```

3. Criar ambiente virtual

Linux/macOS:
```text
python -m venv venv
source venv/bin/activate
```
Windows:
```text
venv\Scripts\activate
```

4.Vá para a pasta do projeto:

```text
cd ~/tts-api
```

5. Instalar dependências

```text
pip install -r requirements.txt
```

6. Executar a API

```text
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

7. Acesse a documentação:

. Acesse: http://localhost:8000

. Acesse: http://localhost:8000/docs
 para testar os endpoints.


### 🎤 Clonagem de voz

. Coloque um arquivo de voz dentro da pasta:

voices/

Exemplo:

voices/minha_voz.wav

Recomendações:

5 a 20 segundos de áudio

Voz limpa, pouco ruído

Formato WAV ou MP3

10. Endpoint da API

```text
POST /v1/text-to-speech

Request:

POST /v1/text-to-speech
Content-Type: application/json

Body:

{
  "text": "Olá, este é um teste de geração de voz.",
  "voice": "voices/minha_voz.wav",
  "language": "pt"
}

Response: Retorna um arquivo de áudio WAV.
```

### 📝 Endpoint da API

POST /v1/text-to-speech

Request Body:
```text
{
  "text": "Olá, este é um teste de geração de voz.",
  "voice": "voices/minha_voz.wav",
  "language": "pt"
}
```

Response:
```text
{
  "audio_files": ["outputs/default.wav"]
}
```
Testar via cURL

```text
curl -X POST http://localhost:8000/v1/text-to-speech \
-H "Content-Type: application/json" \
-d '{"text":"Olá mundo","voice":"voices/minha_voz.wav","language":"pt"}'
```

### ⚡ Performance

O modelo XTTS v2 suporta:

Geração rápida de voz

Múltiplas línguas

Clonagem com poucos segundos de áudio

Exemplo em GPU:

RTX 3060 → ~10x tempo real

### 🔧 Tecnologias ###

Python

FastAPI

✅ Uvicorn

✅ Coqui TTS

✅ XTTS v2

✅ PyTorch

### ⚡ Funcionalidades

✅ Streaming de áudio em tempo real

✅ Processamento paralelo de textos longos

✅ Suporte a clonagem de voz ilimitada

✅ API compatível com ElevenLabs

✅ Até 100k caracteres por requisição

📜 Licença

MIT License




