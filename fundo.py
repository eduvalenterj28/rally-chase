from PPlay.sprite import *
from sprites import *
from config import *
import mundo

# ======================
# VELOCIDADE
# ======================

velocidade_fundo = VELOCIDADE_FUNDO_INICIAL
velocidade_inicial = VELOCIDADE_FUNDO_INICIAL

# ======================
# CARREGAR FUNDO
# ======================

def carregar_fundo_mundo():

    global fundo1
    global fundo2
    global fundo3
    global ALTURA

    # ======================
    # MUNDO 1 - TERRA
    # ======================

    if mundo.mundo_atual == 1:

        if mundo.fase_atual == 1:
            caminho = "sprites/terra1.png"

        elif mundo.fase_atual == 2:
            caminho = "sprites/terra2.png"

        else:
            caminho = "sprites/terra3.png"

    # ======================
    # MUNDO 2 - NEVE
    # ======================

    elif mundo.mundo_atual == 2:

        if mundo.fase_atual == 1:
            caminho = "sprites/neve1.png"

        elif mundo.fase_atual == 2:
            caminho = "sprites/neve2.png"

        else:
            caminho = "sprites/neve3.png"

    # ======================
    # MUNDO 3 - DESERTO
    # ======================

    else:

        if mundo.fase_atual == 1:
            caminho = "sprites/deserto1.png"

        elif mundo.fase_atual == 2:
            caminho = "sprites/deserto2.png"

        else:
            caminho = "sprites/deserto3.png"

    fundo1 = Sprite(caminho)
    fundo2 = Sprite(caminho)
    fundo3 = Sprite(caminho)

    ALTURA = fundo1.height

    fundo1.x = 0
    fundo1.y = 0

    fundo2.x = 0
    fundo2.y = -ALTURA

    fundo3.x = 0
    fundo3.y = -2 * ALTURA

# ======================
# INICIALIZAÇÃO
# ======================

carregar_fundo_mundo()

# ======================
# MOVIMENTO
# ======================

def mover_fundos(dt):

    fundo1.y += velocidade_fundo * dt
    fundo2.y += velocidade_fundo * dt
    fundo3.y += velocidade_fundo * dt

    if fundo1.y >= ALTURA:
        fundo1.y = fundo3.y - ALTURA

    if fundo2.y >= ALTURA:
        fundo2.y = fundo1.y - ALTURA

    if fundo3.y >= ALTURA:
        fundo3.y = fundo2.y - ALTURA

# ======================
# DESENHO
# ======================

def desenhar_fundos():

    fundo1.set_position(
        0,
        round(fundo1.y)
    )

    fundo2.set_position(
        0,
        round(fundo2.y)
    )

    fundo3.set_position(
        0,
        round(fundo3.y)
    )

    fundo1.draw()
    fundo2.draw()
    fundo3.draw()

# ======================
# RESET
# ======================

def resetar_fundos():

    global velocidade_fundo

    velocidade_fundo = VELOCIDADE_FUNDO_INICIAL

    carregar_fundo_mundo()