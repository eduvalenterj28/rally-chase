from config import *

# ======================
# TEMPO
# ======================

tempo_total = 0


def atualizar_timer(dt):

    global tempo_total

    tempo_total += dt


def desenhar_timer(janela):

    minutos = int(tempo_total // 60)
    segundos = int(tempo_total % 60)
    milisegundos = int((tempo_total % 1) * 1000)

    texto = (
        f"{minutos:02d}:"
        f"{segundos:02d}:"
        f"{milisegundos:03d}"
    )

    janela.draw_text(
        texto,
        LARGURA_JANELA - 220,
        20,
        size=35,
        color=(255, 255, 255),
        font_name="Arial"
    )