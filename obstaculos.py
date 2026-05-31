from PPlay.sprite import *
from sprites import *
from car import *
import fundo
import random

# ======================
# LISTA DE OBSTACULOS
# ======================

obstaculos = []

# ======================
# CONFIGURACOES
# ======================

VELOCIDADE_NORMAL = 300
VELOCIDADE_REDUZIDA = 120

tempo_reduzido = 0

# spawn
tempo_spawn = 0
intervalo_min = 1.0
intervalo_max = 2.2
proximo_spawn = random.uniform(
    intervalo_min,
    intervalo_max
)

# limites da pista
# ajuste fino depois se precisar
PISTA_X_MIN = 260
PISTA_X_MAX = 740


# ======================
# CRIAR OBSTACULO
# ======================

def criar_obstaculo():

    modelos = [
        "sprites/pedra.png",
        "sprites/barreira.png"
    ]

    caminho = random.choice(modelos)

    obs = Sprite(caminho)

    # posição aleatória dentro da pista
    obs.x = random.randint(
        int(PISTA_X_MIN),
        int(PISTA_X_MAX - obs.width)
    )

    # nasce acima da tela
    obs.y = -obs.height

    obstaculos.append(obs)


# ======================
# MOVIMENTO + COLISAO
# ======================

def mover_obstaculos(dt):

    global tempo_spawn
    global proximo_spawn
    global tempo_reduzido

    # ------------------
    # SPAWN
    # ------------------

    tempo_spawn += dt

    if tempo_spawn >= proximo_spawn:

        criar_obstaculo()

        tempo_spawn = 0

        proximo_spawn = random.uniform(
            intervalo_min,
            intervalo_max
        )

    # ------------------
    # MOVIMENTO
    # ------------------

    for obs in obstaculos[:]:

        # usa mesma velocidade do fundo
        obs.y += fundo.velocidade_fundo * dt

        # remove ao sair da tela
        if obs.y >= 800:

            obstaculos.remove(obs)
            continue

        # ------------------
        # COLISAO AJUSTADA
        # ------------------

        margem_carro_x = 35
        margem_carro_y = 25

        margem_obs_x = 25
        margem_obs_y = 25

        colisao = (

            car.x + margem_carro_x <
            obs.x + obs.width - margem_obs_x

            and

            car.x + car.width - margem_carro_x >
            obs.x + margem_obs_x

            and

            car.y + margem_carro_y <
            obs.y + obs.height - margem_obs_y

            and

            car.y + car.height - margem_carro_y >
            obs.y + margem_obs_y
        )

        if colisao:

            tempo_reduzido = 3

            # reduz velocidade do fundo
            fundo.velocidade_fundo = VELOCIDADE_REDUZIDA

    # ------------------
    # EFEITO DE SLOW
    # ------------------

    if tempo_reduzido > 0:

        tempo_reduzido -= dt

    else:

        # recuperação gradual
        if fundo.velocidade_fundo < VELOCIDADE_NORMAL:

            fundo.velocidade_fundo += 80 * dt

            if fundo.velocidade_fundo > VELOCIDADE_NORMAL:

                fundo.velocidade_fundo = VELOCIDADE_NORMAL


# ======================
# DESENHO
# ======================

def desenhar_obstaculos():

    for obs in obstaculos:

        obs.set_position(
            round(obs.x),
            round(obs.y)
        )

        obs.draw()