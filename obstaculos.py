from PPlay.sprite import *
from sprites import *
from car import *
from config import *
import fundo
import random

from formacoes import *

# ======================
# LISTA DE OBSTACULOS
# ======================

obstaculos = []

tempo_reduzido = 0

tempo_spawn = 0

proximo_spawn = random.uniform(
    INTERVALO_SPAWN_MIN,
    INTERVALO_SPAWN_MAX
)

# ======================
# TRONCO ESPECIAL
# ======================

def criar_tronco():

    obs = Sprite("sprites/tronco.png")

    lado_livre = random.choice([
        "esquerda",
        "direita"
    ])

    if lado_livre == "esquerda":

        obs.x = 390

    else:

        obs.x = 260

    obs.y = -obs.height

    obstaculos.append(
        {
            "sprite": obs,
            "tipo": "tronco"
        }
    )

# ======================
# FORMACAO NORMAL
# ======================

def criar_formacao():

    formacao = obter_formacao()

    tipos = [

        ("sprites/pedra.png", "pedra"),
        ("sprites/pedra.png", "pedra"),

        ("sprites/pedra2.png", "pedra2"),

        ("sprites/barreira.png", "barreira"),
        ("sprites/barreira.png", "barreira"),

        ("sprites/buraco.png", "buraco")

    ]

    arquivo, tipo = random.choice(tipos)

    y_inicial = -100

    for linha in range(len(formacao)):

        for faixa in range(3):

            if formacao[linha][faixa] == 1:

                obs = Sprite(arquivo)

                obs.x = (
                    FAIXAS[faixa]
                    - obs.width / 2
                )

                obs.y = (
                    y_inicial
                    - linha * ESPACAMENTO_Y
                )

                obstaculos.append(
                    {
                        "sprite": obs,
                        "tipo": tipo
                    }
                )

# ======================
# HITBOX DOS OBSTACULOS
# ======================

def obter_hitbox_obstaculo(tipo):

    # PEDRA

    if tipo == "pedra":

        return (
            45,
            40
        )

    # PEDRA 2

    if tipo == "pedra2":

        return (
            45,
            35
        )

    # BARREIRA

    if tipo == "barreira":

        return (
            30,
            50
        )

    # BURACO

    if tipo == "buraco":

        return (
            30,
            25
        )

    # TRONCO

    if tipo == "tronco":

        return (
            90,
            25
        )

    return (
        25,
        25
    )

# ======================
# MOVIMENTO
# ======================

def mover_obstaculos(dt):

    global tempo_spawn
    global proximo_spawn
    global tempo_reduzido

    tempo_spawn += dt

    if tempo_spawn >= proximo_spawn:

        if random.random() < CHANCE_TRONCO:

            criar_tronco()

            tempo_spawn = 0

            proximo_spawn = random.uniform(
                INTERVALO_TRONCO_MIN,
                INTERVALO_TRONCO_MAX
            )

        else:

            criar_formacao()

            tempo_spawn = 0

            proximo_spawn = random.uniform(
                INTERVALO_SPAWN_MIN,
                INTERVALO_SPAWN_MAX
            )

    # ======================
    # MOVIMENTO + COLISAO
    # ======================

    for item in obstaculos[:]:

        obs = item["sprite"]
        tipo = item["tipo"]

        obs.y += fundo.velocidade_fundo * dt

        if obs.y >= ALTURA_JANELA + 200:

            obstaculos.remove(item)
            continue

        # ======================
        # HITBOX DO CARRO
        # ======================

        car_left = car.x + HITBOX_X
        car_right = car_left + HITBOX_W

        car_top = car.y + HITBOX_Y
        car_bottom = car_top + HITBOX_H

        # ======================
        # HITBOX DO OBSTACULO
        # ======================

        margem_obs_x, margem_obs_y = (
            obter_hitbox_obstaculo(tipo)
        )

        obs_left = obs.x + margem_obs_x
        obs_right = obs.x + obs.width - margem_obs_x

        obs_top = obs.y + margem_obs_y
        obs_bottom = obs.y + obs.height - margem_obs_y

        colisao = (

            car_left < obs_right

            and

            car_right > obs_left

            and

            car_top < obs_bottom

            and

            car_bottom > obs_top
        )

        if colisao:

            tempo_reduzido = TEMPO_REDUZIDO

            fundo.velocidade_fundo = (
                VELOCIDADE_REDUZIDA
            )

    # ======================
    # RECUPERACAO
    # ======================

    if tempo_reduzido > 0:

        tempo_reduzido -= dt

    else:

        if fundo.velocidade_fundo < VELOCIDADE_FUNDO_INICIAL:

            fundo.velocidade_fundo += (
                RECUPERACAO_VELOCIDADE * dt
            )

            if fundo.velocidade_fundo > VELOCIDADE_FUNDO_INICIAL:

                fundo.velocidade_fundo = (
                    VELOCIDADE_FUNDO_INICIAL
                )

# ======================
# DESENHO
# ======================

def desenhar_obstaculos():

    for item in obstaculos:

        obs = item["sprite"]

        obs.set_position(
            round(obs.x),
            round(obs.y)
        )

        obs.draw()