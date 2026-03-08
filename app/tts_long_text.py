import re

def split_text(text):
    # Divide o texto em sentenças baseadas em pontos, exclamações ou interrogações
    # Isso evita que o modelo XTTS tente processar tudo de uma vez e se perca
    sentences = re.split(r'(?<=[.!?]) +', text)
    # Remove espaços vazios que podem surgir na divisão
    return [s.strip() for s in sentences if s.strip()]
