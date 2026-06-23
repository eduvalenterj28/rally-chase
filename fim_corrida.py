from keys import *
import menu
import fase
import mundo
import timer
import obstaculos
import tela_fase

from sprites import *
from numeros import *

from fundo import resetar_fundos
from car import resetar_carro
from obstaculos import resetar_obstaculos

posicao = 1

space_travado_fim = False
space_travado_fim_campeonato = False


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
    # POSIÇÃO
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

    global space_travado_fim
    global space_travado_fim_campeonato

    if pressionada(SPACE):

        if not space_travado_fim:

            mundo.avancar_fase()

            if mundo.jogo_finalizado():

                menu.estado = menu.FIM_CAMPEONATO

                space_travado_fim = True
                space_travado_fim_campeonato = True

                return

            resetar_fundos()
            resetar_carro()
            resetar_obstaculos()

            fase.resetar_fase()

            timer.tempo_total = 0
            fase.resultado_processado = False

            tela_fase.tempo_tela = 0

            menu.estado = menu.TELA_FASE

            space_travado_fim = True

    else:

        space_travado_fim = False


def desenhar_fim_campeonato():

    fimDoCampeonato.draw()


def resetar_jogo_completo():

    global space_travado_fim
    global space_travado_fim_campeonato

    mundo.resetar_mundo()

    resetar_fundos()
    resetar_carro()
    resetar_obstaculos()

    fase.resetar_fase()

    timer.tempo_total = 0
    fase.resultado_processado = False

    tela_fase.tempo_tela = 0
    tela_fase.blink_timer = 0

    space_travado_fim = False
    space_travado_fim_campeonato = True

    menu.space_travado_menu = True
    menu.estado = menu.MENU


def atualizar_fim_campeonato():

    global space_travado_fim_campeonato

    if pressionada(SPACE):

        if not space_travado_fim_campeonato:

            resetar_jogo_completo()

    else:

        space_travado_fim_campeonato = False