from PPlay.sprite import *
from sprites import *

# velocidade da pista
velocidade_fundo = 300
velocidade_inicial = 300

ALTURA = fundo1.height

# posicionamento inicial
fundo1.x = 0
fundo1.y = 0

fundo2.x = 0
fundo2.y = -ALTURA

fundo3.x = 0
fundo3.y = -2 * ALTURA


def mover_fundos(dt):

    # movimento
    fundo1.y += velocidade_fundo * dt
    fundo2.y += velocidade_fundo * dt
    fundo3.y += velocidade_fundo * dt

    # reposicionamento
    if fundo1.y >= ALTURA:
        fundo1.y = fundo3.y - ALTURA

    if fundo2.y >= ALTURA:
        fundo2.y = fundo1.y - ALTURA

    if fundo3.y >= ALTURA:
        fundo3.y = fundo2.y - ALTURA


def desenhar_fundos():

    fundo1.set_position(0, round(fundo1.y))
    fundo2.set_position(0, round(fundo2.y))
    fundo3.set_position(0, round(fundo3.y))

    fundo1.draw()
    fundo2.draw()
    fundo3.draw()