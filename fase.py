# ======================
# FASE 1
# ======================

distancia = 0

DISTANCIA_FASE = 36000

fase_concluida = False


# ======================
# ATUALIZAÇÃO
# ======================

def atualizar_fase(dt, velocidade):

    global distancia
    global fase_concluida

    if fase_concluida:
        return

    distancia += velocidade * dt

    if distancia >= DISTANCIA_FASE:

        distancia = DISTANCIA_FASE
        fase_concluida = True


# ======================
# PROGRESSO
# ======================

def obter_progresso():

    return distancia / DISTANCIA_FASE


# ======================
# RESET
# ======================

def resetar_fase():

    global distancia
    global fase_concluida

    distancia = 0
    fase_concluida = False