from window import *
from fundo import *
from car import *
from obstaculos import *
from timer import *
import menu

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
        mover_carro(dt)
        mover_obstaculos(dt)
        atualizar_timer(dt)

        desenhar_fundos()
        desenhar_obstaculos()
        desenhar_carro()
        desenhar_timer(janela)

    janela.update()