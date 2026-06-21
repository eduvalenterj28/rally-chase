# ======================
# MUNDO E FASE
# ======================

mundo_atual = 1
fase_atual = 1

TOTAL_MUNDOS = 3
FASES_POR_MUNDO = 3

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
# FIM DO JOGO
# ======================

def jogo_finalizado():

    return mundo_atual > TOTAL_MUNDOS