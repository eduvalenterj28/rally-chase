from window import *
from sprites import *
from fundo import *

while True:

    dt = janela.delta_time()

    mover_fundos(dt)

    desenhar_fundos()
    car.draw()

    # atualiza a janela
    janela.update()