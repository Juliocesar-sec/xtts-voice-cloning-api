from fastapi.responses import StreamingResponse


def stream_audio(file_path: str):
    """
    Faz streaming de um arquivo de áudio WAV.
    """

    def audio_generator():
        with open(file_path, "rb") as f:
            yield f.read()

    return StreamingResponse(audio_generator(), media_type="audio/wav")
