import mundo

# ======================
# DISTÂNCIA DE CADA FASE
# ======================

DISTANCIAS_FASES = {

    (1, 1): 1500,
    (1, 2): 1800,
    (1, 3): 2100,

    (2, 1): 2400,
    (2, 2): 2700,
    (2, 3): 3000,

    (3, 1): 3300,
    (3, 2): 3600,
    (3, 3): 4000
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