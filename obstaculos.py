from PPlay.sprite import *
import fase
import mundo

from sprites import *
from car import *
from config import *
from dificuldade import *

import fundo
import random
import som

from formacoes import *

# ======================
# LISTA DE OBSTÁCULOS
# ======================

obstaculos = []

# ======================
# CONTROLE DE SPAWN
# ======================

distancia_spawn = 0
proximo_spawn_distancia = 0

# distância mínima em pixels entre um grupo de obstáculos e outro
DISTANCIA_MINIMA_ENTRE_SPAWNS = 900

# impede spawn enquanto ainda existe objeto muito perto do topo
LIMITE_AREA_SPAWN = 250

# margem visual para evitar que sprites grandes encostem uns nos outros
MARGEM_VISUAL_X = 12
MARGEM_VISUAL_Y = 12

# ======================
# CONTROLE DE ERRO
# ======================

tempo_reduzido = 0
erros = 0
cooldown_erro = 0


# ======================
# SORTEIO DO PRÓXIMO SPAWN
# ======================

def sortear_proximo_spawn():

    spawn_min, spawn_max = obter_intervalo_spawn()

    try:
        velocidade_base = fundo.obter_velocidade_inicial_atual()
    except:
        velocidade_base = VELOCIDADE_FUNDO_INICIAL

    distancia_min = spawn_min * velocidade_base
    distancia_max = spawn_max * velocidade_base

    distancia_sorteada = random.uniform(
        distancia_min,
        distancia_max
    )

    if distancia_sorteada < DISTANCIA_MINIMA_ENTRE_SPAWNS:
        distancia_sorteada = DISTANCIA_MINIMA_ENTRE_SPAWNS

    return distancia_sorteada


proximo_spawn_distancia = sortear_proximo_spawn()


# ======================
# SPRITES POR MUNDO
# ======================

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


# ======================
# ÁREA DE SPAWN
# ======================

def area_spawn_livre():

    for item in obstaculos:

        obs = item["sprite"]

        if obs.y < LIMITE_AREA_SPAWN:
            return False

    return True


def retangulos_sobrepostos(a, b):

    a_left = a.x + MARGEM_VISUAL_X
    a_right = a.x + a.width - MARGEM_VISUAL_X
    a_top = a.y + MARGEM_VISUAL_Y
    a_bottom = a.y + a.height - MARGEM_VISUAL_Y

    b_left = b.x + MARGEM_VISUAL_X
    b_right = b.x + b.width - MARGEM_VISUAL_X
    b_top = b.y + MARGEM_VISUAL_Y
    b_bottom = b.y + b.height - MARGEM_VISUAL_Y

    return (
        a_left < b_right and
        a_right > b_left and
        a_top < b_bottom and
        a_bottom > b_top
    )


def pode_adicionar_na_linha(novo_obstaculo, obstaculos_linha):

    for outro in obstaculos_linha:

        if retangulos_sobrepostos(novo_obstaculo, outro):
            return False

    return True


# ======================
# CRIAÇÃO DE OBSTÁCULOS
# ======================

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


def escolher_tipo_obstaculo():

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

    return random.choice(tipos)


def criar_formacao():

    formacao = obter_formacao()

    y_inicial = -100

    for linha in range(len(formacao)):

        obstaculos_linha = []

        arquivo, tipo = escolher_tipo_obstaculo()

        for faixa in range(3):

            if formacao[linha][faixa] == 1:

                obs = Sprite(arquivo)

                obs.x = FAIXAS[faixa] - obs.width / 2
                obs.y = y_inicial - linha * ESPACAMENTO_Y

                if pode_adicionar_na_linha(obs, obstaculos_linha):

                    obstaculos.append({
                        "sprite": obs,
                        "tipo": tipo
                    })

                    obstaculos_linha.append(obs)


# ======================
# HITBOX
# ======================

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


# ======================
# MOVIMENTO E COLISÃO
# ======================

def mover_obstaculos(dt):

    global distancia_spawn
    global proximo_spawn_distancia
    global tempo_reduzido
    global erros
    global cooldown_erro

    cooldown_erro -= dt

    if fundo.velocidade_fundo > 0 and not fase.desacelerando:

        distancia_spawn += fundo.velocidade_fundo * dt

    if (
        fase.obter_porcentagem() < 98
        and distancia_spawn >= proximo_spawn_distancia
        and area_spawn_livre()
    ):

        chance_tronco = obter_chance_tronco()

        if random.random() < chance_tronco:
            criar_tronco()
        else:
            criar_formacao()

        distancia_spawn = 0
        proximo_spawn_distancia = sortear_proximo_spawn()

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

            som.tocar_hit()

            tempo_reduzido = TEMPO_REDUZIDO
            fundo.velocidade_fundo = VELOCIDADE_REDUZIDA

            erros += 1
            cooldown_erro = 1.0

    if tempo_reduzido > 0:

        tempo_reduzido -= dt

    else:

        if (
            not fase.desacelerando
            and fundo.velocidade_fundo < fundo.obter_velocidade_inicial_atual()
        ):

            fundo.velocidade_fundo += RECUPERACAO_VELOCIDADE * dt

            if fundo.velocidade_fundo > fundo.obter_velocidade_inicial_atual():
                fundo.velocidade_fundo = fundo.obter_velocidade_inicial_atual()


# ======================
# DESENHO
# ======================

def desenhar_obstaculos():

    for item in obstaculos:

        obs = item["sprite"]

        obs.set_position(round(obs.x), round(obs.y))
        obs.draw()


# ======================
# RESET
# ======================

def resetar_obstaculos():

    global distancia_spawn
    global proximo_spawn_distancia
    global tempo_reduzido
    global erros
    global cooldown_erro

    obstaculos.clear()

    distancia_spawn = 0
    tempo_reduzido = 0
    erros = 0
    cooldown_erro = 0

    proximo_spawn_distancia = sortear_proximo_spawn()