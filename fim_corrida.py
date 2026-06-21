from sprites import *
import timer

# ======================
# POSIÇÃO FINAL
# ======================

posicao = 1

# ======================
# CALCULA POSIÇÃO
# ======================

def gerar_posicao():

    global posicao

    tempo = timer.tempo_total

    if tempo <= 120:
        posicao = 1

    elif tempo <= 130:
        posicao = 2

    elif tempo <= 140:
        posicao = 3

    elif tempo <= 150:
        posicao = 4

    elif tempo <= 160:
        posicao = 5

    elif tempo <= 170:
        posicao = 6

    elif tempo <= 180:
        posicao = 7

    else:
        posicao = 8


# ======================
# DESENHO
# ======================

def desenhar_fim(janela):

    fimDeJogo.draw()

    minutos = int(timer.tempo_total // 60)
    segundos = int(timer.tempo_total % 60)
    milisegundos = int(
        (timer.tempo_total % 1) * 1000
    )

    tempo_texto = (
        f"{minutos:02d}:"
        f"{segundos:02d}:"
        f"{milisegundos:03d}"
    )

    # ------------------
    # POSIÇÃO
    # ------------------

    janela.draw_text(
        f"{posicao}º",
        355,
        500,
        size=78,
        color=(255, 200, 0),
        font_name="Arial Black"
    )

    # ------------------
    # TEMPO
    # ------------------

    janela.draw_text(
        tempo_texto,
        505,
        500,
        size=42,
        color=(255, 140, 40),
        font_name="Consolas"
    )