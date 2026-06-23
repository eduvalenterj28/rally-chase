import mundo

# ======================
# DISTÂNCIA DE CADA FASE
# ======================

DISTANCIAS_FASES = {

    (1, 1): 33000,  # ~1min50s
    (1, 2): 34500,  # ~1min55s
    (1, 3): 36000,  # ~2min

    (2, 1): 36000,  # ~2min
    (2, 2): 37500,  # ~2min05s
    (2, 3): 39000,  # ~2min10s 39000

    (3, 1): 39000,  # ~2min10s 39000
    (3, 2): 40500,  # ~2min15s 40500
    (3, 3): 42000   # ~2min20s 42000
}

# ======================
# PROGRESSO DA FASE
# ======================

distancia = 0

fase_concluida = False

resultado_processado = False

desacelerando = False

# ======================
# DISTÂNCIA ATUAL
# ======================

def obter_distancia_fase():

    return DISTANCIAS_FASES[
        (
            mundo.mundo_atual,
            mundo.fase_atual
        )
    ]

# ======================
# ATUALIZAÇÃO
# ======================

def atualizar_fase(dt, velocidade):

    global distancia
    global desacelerando

    if fase_concluida:
        return

    if desacelerando:
        return

    distancia += velocidade * dt

    if distancia >= obter_distancia_fase():

        distancia = obter_distancia_fase()

        desacelerando = True

# ======================
# PORCENTAGEM
# ======================

def obter_porcentagem():

    return min(
        100,
        int(
            (
                distancia /
                obter_distancia_fase()
            ) * 100
        )
    )

# ======================
# PROGRESSO
# ======================

def obter_progresso():

    return (
        distancia /
        obter_distancia_fase()
    )

# ======================
# TEXTO DA FASE
# ======================

def texto_fase():

    return (
        f"M{mundo.mundo_atual}"
        f"-F{mundo.fase_atual}"
    )

# ======================
# RESET
# ======================

def resetar_fase():

    global distancia
    global fase_concluida
    global resultado_processado
    global desacelerando

    distancia = 0

    fase_concluida = False

    resultado_processado = False

    desacelerando = False

def texto_porcentagem():

    return str(
        obter_porcentagem()
    )