from sprites import *
from keys import *

import menu
import mundo

tempo_tela = 0

def obter_tela():

    if mundo.mundo_atual == 1:

        if mundo.fase_atual == 1:
            return faseFloresta1
        elif mundo.fase_atual == 2:
            return faseFloresta2
        else:
            return faseFloresta3

    elif mundo.mundo_atual == 2:

        if mundo.fase_atual == 1:
            return faseNeve1
        elif mundo.fase_atual == 2:
            return faseNeve2
        else:
            return faseNeve3

    else:

        if mundo.fase_atual == 1:
            return faseDeserto1
        elif mundo.fase_atual == 2:
            return faseDeserto2
        else:
            return faseDeserto3


def desenhar_tela_fase():

    obter_tela().draw()


def atualizar_tela_fase(dt):

    global tempo_tela

    tempo_tela += dt

    # espera meio segundo antes de aceitar espaço

    if tempo_tela < 0.5:
        return

    if pressionada(SPACE):

        tempo_tela = 0

        menu.estado = menu.JOGO