from window import *
from fundo import *
from car import *
from obstaculos import *
from timer import *
from fim_corrida import *
from tela_fase import *
from numeros import *
from sprites import *
from keys import *

import fundo
import menu
import fase
import som

esc_travado = False

while True:

    dt = janela.delta_time()

    # ======================
    # CONTROLE DE PAUSE
    # ======================

    if pressionada(ESC):

        if not esc_travado:

            if menu.estado == menu.JOGO:

                som.parar_motor()
                som.pausar_musica_jogo()

                menu.estado = menu.PAUSE

            elif menu.estado == menu.PAUSE:

                som.continuar_musica_jogo()

                menu.estado = menu.JOGO

            esc_travado = True

    else:

        esc_travado = False

    # ======================
    # MENU
    # ======================

    if menu.estado == menu.MENU:

        som.atualizar_motor(False)

        menu.desenhar_menu()
        menu.atualizar_menu()

    # ======================
    # TELA DA FASE
    # ======================

    elif menu.estado == menu.TELA_FASE:

        som.atualizar_motor(False)

        desenhar_tela_fase()
        atualizar_tela_fase(dt)

    # ======================
    # JOGO
    # ======================

    elif menu.estado == menu.JOGO:

        if fase.desacelerando:

            fundo.velocidade_fundo -= 200 * dt

            if fundo.velocidade_fundo <= 0:
                fundo.velocidade_fundo = 0
                fase.fase_concluida = True

        # ======================
        # SOM DO MOTOR
        # ======================

        if fundo.velocidade_fundo > 0 and not fase.fase_concluida:
            som.atualizar_motor(True)
        else:
            som.atualizar_motor(False)

        mover_fundos(dt)

        fase.atualizar_fase(dt, fundo.velocidade_fundo)

        mover_carro(dt)
        mover_obstaculos(dt)

        atualizar_timer(dt)

        desenhar_fundos()
        desenhar_obstaculos()
        desenhar_carro()

        # ======================
        # HUD
        # ======================

        desenhar_timer(janela)

        desenhar_numero(
            str(fase.obter_porcentagem()) + "%",
            40,
            20
        )

        # ======================
        # FIM DA FASE
        # ======================

        if fase.fase_concluida:

            if not fase.resultado_processado:
                gerar_posicao()
                fase.resultado_processado = True

            som.parar_motor()
            som.parar_musica_jogo()

            menu.estado = menu.FIM

    # ======================
    # PAUSE
    # ======================

    elif menu.estado == menu.PAUSE:

        som.atualizar_motor(False)

        pause.draw()

    # ======================
    # FIM DE CORRIDA
    # ======================

    elif menu.estado == menu.FIM:

        som.atualizar_motor(False)

        desenhar_fim(janela)
        atualizar_fim()

    # ======================
    # FIM DO CAMPEONATO
    # ======================

    elif menu.estado == menu.FIM_CAMPEONATO:

        som.atualizar_motor(False)

        desenhar_fim_campeonato()
        atualizar_fim_campeonato()

    janela.update()