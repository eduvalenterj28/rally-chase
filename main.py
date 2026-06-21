from window import *
from fundo import *
from car import *
from obstaculos import *
from timer import *
from fim_corrida import *
from tela_fase import *
from numeros import *

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
    # TELA DA FASE
    # ======================

    elif menu.estado == menu.TELA_FASE:

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

        # 🔥 FIX FINAL: % garantido via sprite correto
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

            menu.estado = menu.FIM

    # ======================
    # FIM DE CORRIDA
    # ======================

    elif menu.estado == menu.FIM:

        desenhar_fim(janela)
        atualizar_fim()

    janela.update()