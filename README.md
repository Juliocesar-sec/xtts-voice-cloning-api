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

### 📄 Conteúdo de cada arquivo app/*.py

```text
app/__init__.py

Arquivo vazio, usado para definir app como um pacote Python.
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




