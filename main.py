from window import *
from sprites import *
from fundo import *
from car import *

while True:

    dt = janela.delta_time()

    mover_fundos(dt)
    mover_carro(dt)

    desenhar_fundos()
    desenhar_carro()

    # atualiza a janela
    janela.update()