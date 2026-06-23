# ======================
# MUNDO E FASE
# ======================

mundo_atual = 1
fase_atual = 1

TOTAL_MUNDOS = 3
FASES_POR_MUNDO = 3

MULTIPLICADOR_VELOCIDADE_MUNDO = 1.1

# ======================
# VELOCIDADE POR MUNDO
# ======================

def obter_multiplicador_velocidade():

    return MULTIPLICADOR_VELOCIDADE_MUNDO ** (mundo_atual - 1)

# ======================
# AVANÇAR FASE
# ======================

def avancar_fase():

    global mundo_atual
    global fase_atual

    fase_atual += 1

    if fase_atual > FASES_POR_MUNDO:

        fase_atual = 1
        mundo_atual += 1

# ======================
# RESETAR MUNDO
# ======================

def resetar_mundo():

    global mundo_atual
    global fase_atual

    mundo_atual = 1
    fase_atual = 1

# ======================
# FIM DO JOGO
# ======================

def jogo_finalizado():

    return mundo_atual > TOTAL_MUNDOS