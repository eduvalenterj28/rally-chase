from window import *
from sprites import *
from fundo import *
from car import *
from obstaculos import *
from timer import *

while True:

    dt = janela.delta_time()

    mover_fundos(dt)
    mover_obstaculos(dt)
    mover_carro(dt)

    atualizar_timer(dt)

    desenhar_fundos()
    desenhar_obstaculos()
    desenhar_carro()
    desenhar_timer(janela)

    # atualiza a janela
    janela.update()