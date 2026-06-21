from window import *
from fundo import *
from car import *
from obstaculos import *
from timer import *
from fim_corrida import *

import fundo
import menu
import fase

while True:

    dt = janela.delta_time()

    # ======================
    # MENU
    # ======================

    if menu.estado == menu.MENU:

        menu.desenhar_menu()
        menu.atualizar_menu()

    # ======================
    # JOGO
    # ======================

    elif menu.estado == menu.JOGO:

        # ------------------
        # DESACELERAÇÃO FINAL
        # ------------------

        if fase.desacelerando:

            fundo.velocidade_fundo -= 200 * dt

            if fundo.velocidade_fundo <= 0:

                fundo.velocidade_fundo = 0

                fase.fase_concluida = True

        mover_fundos(dt)

        fase.atualizar_fase(
            dt,
            fundo.velocidade_fundo
        )

        mover_carro(dt)
        mover_obstaculos(dt)

        atualizar_timer(dt)

        desenhar_fundos()
        desenhar_obstaculos()
        desenhar_carro()

        desenhar_timer(janela)

        # ------------------
        # FIM DA FASE
        # ------------------

        if fase.fase_concluida:

            if not fase.resultado_processado:

                gerar_posicao()

                fase.resultado_processado = True

            menu.estado = menu.FIM

    # ======================
    # FIM DE CORRIDA
    # ======================

    elif menu.estado == menu.FIM:

        desenhar_fim(janela)
        atualizar_fim()

    janela.update()