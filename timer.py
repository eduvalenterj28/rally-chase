from config import *
from numeros import *

# ======================
# TEMPO
# ======================

tempo_total = 0

# ======================
# ATUALIZAÇÃO
# ======================

def atualizar_timer(dt):

    global tempo_total
    tempo_total += dt

# ======================
# DESENHO
# ======================

def desenhar_timer(janela):

    minutos = int(tempo_total // 60)
    segundos = int(tempo_total % 60)
    milisegundos = int((tempo_total % 1) * 1000)

    # formato compacto (importante para não estourar tela)
    texto = (
        f"{minutos:02d}"
        f":"
        f"{segundos:02d}"
        f":"
        f"{milisegundos:03d}"
    )

    # posição ajustada para 1000x800
    desenhar_numero(
        texto,
        700,   # puxei para esquerda
        20
    )