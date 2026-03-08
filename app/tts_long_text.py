import re

def split_text(text):
    sentences = re.split(r'(?<=[.!?]) +', text)
    return sentences
