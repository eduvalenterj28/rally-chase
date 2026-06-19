import random

# ======================
# FAIXAS DA PISTA
# ======================

FAIXA_ESQ = 320
FAIXA_CEN = 500
FAIXA_DIR = 680

FAIXAS = [
    FAIXA_ESQ,
    FAIXA_CEN,
    FAIXA_DIR
]

# ======================
# ESPACAMENTO ENTRE LINHAS
# ======================

ESPACAMENTO_Y = 450

# ======================
# FORMACOES
# ======================

FORMACOES = [

    # reta esquerda livre

    [
        [0,1,1],
        [0,1,1]
    ],

    # reta centro livre

    [
        [1,0,1],
        [1,0,1]
    ],

    # reta direita livre

    [
        [1,1,0],
        [1,1,0]
    ],

    # esquerda -> centro

    [
        [0,1,1],
        [1,0,1]
    ],

    # centro -> esquerda

    [
        [1,0,1],
        [0,1,1]
    ],

    # centro -> direita

    [
        [1,0,1],
        [1,1,0]
    ],

    # direita -> centro

    [
        [1,1,0],
        [1,0,1]
    ],

    # esquerda -> direita

    [
        [0,1,1],
        [1,1,0]
    ],

    # direita -> esquerda

    [
        [1,1,0],
        [0,1,1]
    ]
]


def obter_formacao():

    return random.choice(FORMACOES)