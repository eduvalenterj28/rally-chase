from window import *
from sprites import *
from fundo import *
from car import *
from obstaculos import *

while True:

    dt = janela.delta_time()

    mover_fundos(dt)
    mover_obstaculos(dt)
    mover_carro(dt)

    desenhar_fundos()
    desenhar_obstaculos()
    desenhar_carro()

    # atualiza a janela
    janela.update()