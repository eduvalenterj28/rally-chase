from sprites import *
from keys import *

import menu
import mundo
import som

tempo_tela = 0
blink_timer = 0

space_travado_tela_fase = False


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

    global blink_timer

    blink_timer += 1

    if (blink_timer // 20) % 2 == 0:

        pressSpace.set_position(
            350,
            670
        )

        pressSpace.draw()


def atualizar_tela_fase(dt):

    global tempo_tela
    global space_travado_tela_fase

    tempo_tela += dt

    if pressionada(SPACE):

        if (
            tempo_tela >= 0.5
            and not space_travado_tela_fase
        ):

            som.tocar_click()

            tempo_tela = 0
            menu.estado = menu.JOGO

            space_travado_tela_fase = True

        else:

            space_travado_tela_fase = True

    else:

        space_travado_tela_fase = False