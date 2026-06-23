from sprites import *
from keys import *

import som

MENU = 0
TELA_FASE = 1
JOGO = 2
FIM = 3
PAUSE = 4
FIM_CAMPEONATO = 5

estado = MENU

space_travado_menu = False


def atualizar_menu():

    global estado
    global space_travado_menu

    if pressionada(SPACE):

        if not space_travado_menu:

            som.tocar_click()

            estado = TELA_FASE
            space_travado_menu = True

    else:

        space_travado_menu = False


def desenhar_menu():

    menuInicial.draw()