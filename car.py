from sprites import *
from keys import *
from config import *
import fundo

# ======================
# POSIÇÃO INICIAL
# ======================

car.x = (LARGURA_JANELA - car.width) / 2
car.y = ALTURA_JANELA - car.height + 10

# ======================
# PISCA
# ======================

pisca_timer = 0

# ======================
# MOVIMENTO
# ======================

def mover_carro(dt):

    global pisca_timer

    if pressionada(LEFT):
        car.x -= VELOCIDADE_CARRO * dt

    if pressionada(RIGHT):
        car.x += VELOCIDADE_CARRO * dt

    if car.x < 0:
        car.x = 0

    if car.x > LARGURA_JANELA - car.width:
        car.x = LARGURA_JANELA - car.width

    if fundo.velocidade_fundo < VELOCIDADE_FUNDO_INICIAL:
        pisca_timer += dt
    else:
        pisca_timer = 0

# ======================
# DESENHO
# ======================

def desenhar_carro():

    if fundo.velocidade_fundo < VELOCIDADE_FUNDO_INICIAL:

        if int(pisca_timer / INTERVALO_PISCA) % 2 == 0:
            car.draw()

    else:
        car.draw()