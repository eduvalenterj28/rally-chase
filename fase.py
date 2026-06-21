# ======================
# PROGRESSO DA FASE
# ======================

distancia = 0

DISTANCIA_FASE = 3000

fase_concluida = False

resultado_processado = False


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

        print("FASE CONCLUIDA")


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
    global resultado_processado

    distancia = 0

    fase_concluida = False

    resultado_processado = False