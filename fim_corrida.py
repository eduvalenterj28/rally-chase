from keys import *
import menu
import fase
import mundo
import timer

from sprites import *

from fundo import resetar_fundos
from car import resetar_carro
from obstaculos import resetar_obstaculos

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

    janela.draw_text(
        f"{posicao}º",
        355,
        500,
        size=78,
        color=(255, 200, 0),
        font_name="Arial Black"
    )

    janela.draw_text(
        tempo_texto,
        505,
        500,
        size=42,
        color=(255, 140, 40),
        font_name="Consolas"
    )

# ======================
# PRÓXIMA FASE
# ======================

def atualizar_fim():

    if pressionada(SPACE):

        mundo.avancar_fase()

        if mundo.jogo_finalizado():

            return

        resetar_fundos()
        resetar_carro()
        resetar_obstaculos()

        fase.resetar_fase()

        timer.tempo_total = 0

        fase.resultado_processado = False

        menu.estado = menu.JOGO