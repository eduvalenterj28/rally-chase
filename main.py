from window import *
from fundo import *
from car import *
from obstaculos import *
from timer import *
from fim_corrida import *

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

        mover_fundos(dt)

        fase.atualizar_fase(
            dt,
            velocidade_fundo
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

    janela.update()