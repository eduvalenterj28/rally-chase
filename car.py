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
# PISCA (COLISÃO)
# ======================

pisca_timer = 0

# ======================
# OPACIDADE
# ======================

opacidade_carro = 255

# ======================
# FORA DA PISTA
# ======================

def carro_fora_da_pista():

    car_left = car.x + HITBOX_X
    car_right = car_left + HITBOX_W

    fora_esquerda = max(
        0,
        PISTA_X_MIN - car_left
    )

    fora_direita = max(
        0,
        car_right - PISTA_X_MAX
    )

    fora_total = (
        fora_esquerda +
        fora_direita
    )

    limite = (
        HITBOX_W *
        PORCENTAGEM_FORA_PISTA
    )

    return fora_total >= limite

# ======================
# MOVIMENTO
# ======================

def mover_carro(dt):

    global pisca_timer
    global opacidade_carro

    # ------------------
    # MOVIMENTO LATERAL
    # ------------------

    if pressionada(LEFT):
        car.x -= VELOCIDADE_CARRO * dt

    if pressionada(RIGHT):
        car.x += VELOCIDADE_CARRO * dt

    # ------------------
    # LIMITES DA JANELA
    # ------------------

    if car.x < 0:
        car.x = 0

    if car.x > LARGURA_JANELA - car.width:
        car.x = (
            LARGURA_JANELA
            - car.width
        )

    # ------------------
    # FORA DA PISTA
    # ------------------

    if carro_fora_da_pista():

        # transição suave da opacidade

        opacidade_carro -= 300 * dt

        if opacidade_carro < 170:
            opacidade_carro = 170

        # reduz velocidade apenas
        # se não estiver mais lenta
        # por colisão

        if fundo.velocidade_fundo > VELOCIDADE_FORA_PISTA:

            fundo.velocidade_fundo -= 250 * dt

            if (
                fundo.velocidade_fundo <
                VELOCIDADE_FORA_PISTA
            ):

                fundo.velocidade_fundo = (
                    VELOCIDADE_FORA_PISTA
                )

    else:

        # volta gradualmente

        opacidade_carro += 300 * dt

        if opacidade_carro > 255:
            opacidade_carro = 255

        if (
            fundo.velocidade_fundo >
            VELOCIDADE_REDUZIDA
            and
            fundo.velocidade_fundo <
            VELOCIDADE_FUNDO_INICIAL
        ):

            fundo.velocidade_fundo += (
                RECUPERACAO_FORA_PISTA * dt
            )

            if (
                fundo.velocidade_fundo >
                VELOCIDADE_FUNDO_INICIAL
            ):

                fundo.velocidade_fundo = (
                    VELOCIDADE_FUNDO_INICIAL
                )

    # ------------------
    # PISCA DE COLISÃO
    # ------------------

    if fundo.velocidade_fundo < VELOCIDADE_REDUZIDA + 1:

        pisca_timer += dt

    else:

        pisca_timer = 0

# ======================
# DESENHO
# ======================

def desenhar_carro():

    try:
        car.set_alpha(
            int(opacidade_carro)
        )
    except:
        pass

    # pisca apenas em colisão

    if fundo.velocidade_fundo <= VELOCIDADE_REDUZIDA + 1:

        if (
            int(
                pisca_timer /
                INTERVALO_PISCA
            ) % 2 == 0
        ):

            car.draw()

    else:

        car.draw()