from keys import *
import menu
import fase
import mundo
import timer
import obstaculos

from sprites import *
from numeros import *

from fundo import resetar_fundos
from car import resetar_carro
from obstaculos import resetar_obstaculos

posicao = 1

def gerar_posicao():

    global posicao

    erros = obstaculos.erros

    if erros == 0:
        posicao = 1

    elif erros <= 2:
        posicao = 2

    elif erros <= 5:
        posicao = 3

    elif erros <= 7:
        posicao = 4

    else:
        posicao = 5


def desenhar_fim(janela):

    fimDeJogo.draw()

    minutos = int(timer.tempo_total // 60)
    segundos = int(timer.tempo_total % 60)
    milisegundos = int((timer.tempo_total % 1) * 1000)

    tempo_texto = (
        f"{minutos:02d}"
        f":"
        f"{segundos:02d}"
        f":"
        f"{milisegundos:03d}"
    )

    # ======================
    # POSIÇÃO (AJUSTADA)
    # ======================

    sprite_pos = None

    if posicao == 1:
        sprite_pos = Sprite("sprites/1maior.png")

    elif posicao == 2:
        sprite_pos = Sprite("sprites/2maior.png")

    elif posicao == 3:
        sprite_pos = Sprite("sprites/3maior.png")

    elif posicao == 4:
        sprite_pos = Sprite("sprites/4maior.png")

    else:
        sprite_pos = Sprite("sprites/5maior.png")

    sprite_pos.set_position(
        312,
        450
    )

    sprite_pos.draw()

    # ======================
    # TEMPO
    # ======================

    desenhar_numero(
        tempo_texto,
        505,
        460
    )


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

        menu.estado = menu.TELA_FASE