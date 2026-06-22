from PPlay.sprite import *
import fase
import mundo

from sprites import *
from car import *
from config import *
from dificuldade import *

import fundo
import random

from formacoes import *

obstaculos = []

tempo_reduzido = 0
tempo_spawn = 0

erros = 0
cooldown_erro = 0

spawn_min, spawn_max = obter_intervalo_spawn()

proximo_spawn = random.uniform(
    spawn_min,
    spawn_max
)

def obter_pedras_mundo():

    if mundo.mundo_atual == 1:
        return ("sprites/pedra.png", "sprites/pedra2.png")

    elif mundo.mundo_atual == 2:
        return ("sprites/pedraNeve1.png", "sprites/pedraNeve2.png")

    else:
        return ("sprites/pedraDeserto1.png", "sprites/pedraDeserto2.png")

def obter_buraco_mundo():

    if mundo.mundo_atual == 1:
        return "sprites/buraco.png"

    elif mundo.mundo_atual == 2:
        return "sprites/buracoNeve.png"

    else:
        return "sprites/buracoDeserto.png"

def obter_tronco_mundo():

    if mundo.mundo_atual == 1:
        return "sprites/tronco.png"

    elif mundo.mundo_atual == 2:
        return "sprites/troncoNeve.png"

    else:
        return "sprites/troncoDeserto.png"

def criar_tronco():

    obs = Sprite(obter_tronco_mundo())

    lado_livre = random.choice(["esquerda", "direita"])

    if lado_livre == "esquerda":
        obs.x = 390
    else:
        obs.x = 260

    obs.y = -obs.height

    obstaculos.append({
        "sprite": obs,
        "tipo": "tronco"
    })

def criar_formacao():

    formacao = obter_formacao()

    pedra1, pedra2 = obter_pedras_mundo()
    buraco = obter_buraco_mundo()

    tipos = [
        (pedra1, "pedra"),
        (pedra1, "pedra"),
        (pedra2, "pedra2"),
        ("sprites/barreira.png", "barreira"),
        ("sprites/barreira.png", "barreira"),
        (buraco, "buraco")
    ]

    arquivo, tipo = random.choice(tipos)

    y_inicial = -100

    for linha in range(len(formacao)):

        for faixa in range(3):

            if formacao[linha][faixa] == 1:

                obs = Sprite(arquivo)

                obs.x = FAIXAS[faixa] - obs.width / 2
                obs.y = y_inicial - linha * ESPACAMENTO_Y

                obstaculos.append({
                    "sprite": obs,
                    "tipo": tipo
                })

def obter_hitbox_obstaculo(tipo):

    if tipo == "pedra":
        return (45, 40)

    if tipo == "pedra2":
        return (45, 35)

    if tipo == "barreira":
        return (30, 50)

    if tipo == "buraco":
        return (30, 25)

    if tipo == "tronco":
        return (90, 25)

    return (25, 25)

def mover_obstaculos(dt):

    global tempo_spawn
    global proximo_spawn
    global tempo_reduzido
    global erros
    global cooldown_erro

    tempo_spawn += dt
    cooldown_erro -= dt

    if (
        fase.obter_porcentagem() < 98
        and tempo_spawn >= proximo_spawn
    ):

        chance_tronco = obter_chance_tronco()

        if random.random() < chance_tronco:
            criar_tronco()
        else:
            criar_formacao()

        tempo_spawn = 0

        spawn_min, spawn_max = obter_intervalo_spawn()

        proximo_spawn = random.uniform(
            spawn_min,
            spawn_max
        )

    for item in obstaculos[:]:

        obs = item["sprite"]
        tipo = item["tipo"]

        obs.y += fundo.velocidade_fundo * dt

        if obs.y >= ALTURA_JANELA + 200:
            obstaculos.remove(item)
            continue

        car_left = car.x + HITBOX_X
        car_right = car_left + HITBOX_W
        car_top = car.y + HITBOX_Y
        car_bottom = car_top + HITBOX_H

        margem_obs_x, margem_obs_y = obter_hitbox_obstaculo(tipo)

        obs_left = obs.x + margem_obs_x
        obs_right = obs.x + obs.width - margem_obs_x
        obs_top = obs.y + margem_obs_y
        obs_bottom = obs.y + obs.height - margem_obs_y

        colisao = (
            car_left < obs_right and
            car_right > obs_left and
            car_top < obs_bottom and
            car_bottom > obs_top
        )

        if colisao and cooldown_erro <= 0:

            tempo_reduzido = TEMPO_REDUZIDO
            fundo.velocidade_fundo = VELOCIDADE_REDUZIDA

            erros += 1
            cooldown_erro = 1.0

    if tempo_reduzido > 0:
        tempo_reduzido -= dt

    else:

        if (
            not fase.desacelerando
            and fundo.velocidade_fundo < VELOCIDADE_FUNDO_INICIAL
        ):

            fundo.velocidade_fundo += RECUPERACAO_VELOCIDADE * dt

            if fundo.velocidade_fundo > VELOCIDADE_FUNDO_INICIAL:
                fundo.velocidade_fundo = VELOCIDADE_FUNDO_INICIAL

def desenhar_obstaculos():

    for item in obstaculos:

        obs = item["sprite"]

        obs.set_position(round(obs.x), round(obs.y))
        obs.draw()

def resetar_obstaculos():

    global tempo_spawn
    global proximo_spawn
    global tempo_reduzido
    global erros
    global cooldown_erro

    obstaculos.clear()

    tempo_spawn = 0
    tempo_reduzido = 0
    erros = 0
    cooldown_erro = 0

    spawn_min, spawn_max = obter_intervalo_spawn()

    proximo_spawn = random.uniform(
        spawn_min,
        spawn_max
    )