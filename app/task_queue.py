from concurrent.futures import ThreadPoolExecutor

# Apenas 1 por vez para manter a estabilidade do sistema no CPU
executor = ThreadPoolExecutor(max_workers=1)
