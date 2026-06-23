# ======================
# SONS DO JOGO
# ======================

import os

try:
    from pygame import mixer

    if not mixer.get_init():
        mixer.init()

    AUDIO_ATIVO = True
    print("Audio iniciado com sucesso.")

except Exception as erro:
    AUDIO_ATIVO = False
    print("Erro ao iniciar audio:", erro)


# ======================
# PASTA DE AUDIO
# ======================

PASTA_ATUAL = os.path.dirname(os.path.abspath(__file__))
PASTA_MUSICA = os.path.join(PASTA_ATUAL, "musica")

# ======================
# ARQUIVOS POSSIVEIS
# ======================

ARQUIVOS_CLICK = [
    os.path.join(PASTA_MUSICA, "click.wav"),
    os.path.join(PASTA_MUSICA, "click.ogg"),
    os.path.join(PASTA_MUSICA, "click.mp3")
]

ARQUIVOS_MUSICA_MENU = [
    os.path.join(PASTA_MUSICA, "musicaJogo.ogg"),
    os.path.join(PASTA_MUSICA, "musicaJogo.mp3"),
    os.path.join(PASTA_MUSICA, "musicaJogo.wav")
]

ARQUIVOS_MOTOR = [
    os.path.join(PASTA_MUSICA, "motor.wav"),
    os.path.join(PASTA_MUSICA, "motor.ogg"),
    os.path.join(PASTA_MUSICA, "motor.mp3")
]

ARQUIVOS_HIT = [
    os.path.join(PASTA_MUSICA, "hit.wav"),
    os.path.join(PASTA_MUSICA, "hit.ogg"),
    os.path.join(PASTA_MUSICA, "hit.mp3")
]

# ======================
# VOLUMES
# ======================

VOLUME_CLICK = 0.8
VOLUME_MUSICA_MENU = 0.45
VOLUME_MOTOR = 0.35
VOLUME_HIT = 0.8

# ======================
# CONTROLE INTERNO
# ======================

click = None
motor = None
hit = None

musica_menu_tocando = False
motor_tocando = False


def encontrar_arquivo(lista_arquivos):

    for caminho in lista_arquivos:

        if os.path.exists(caminho):
            return caminho

    print("Nenhum arquivo de audio encontrado nesta lista:")

    for caminho in lista_arquivos:
        print(caminho)

    return None


# ======================
# CLICK
# ======================

def carregar_click():

    global click

    if not AUDIO_ATIVO:
        return

    if click is not None:
        return

    caminho_click = encontrar_arquivo(ARQUIVOS_CLICK)

    if caminho_click is None:
        return

    try:
        click = mixer.Sound(caminho_click)
        click.set_volume(VOLUME_CLICK)

        print("Click carregado com sucesso:")
        print(caminho_click)

    except Exception as erro:
        click = None

        print("Erro ao carregar click:")
        print(caminho_click)
        print(erro)


def tocar_click():

    if not AUDIO_ATIVO:
        return

    carregar_click()

    try:
        if click is not None:
            click.play()

    except Exception as erro:
        print("Erro ao tocar click:", erro)


# ======================
# HIT / COLISÃO
# ======================

def carregar_hit():

    global hit

    if not AUDIO_ATIVO:
        return

    if hit is not None:
        return

    caminho_hit = encontrar_arquivo(ARQUIVOS_HIT)

    if caminho_hit is None:
        return

    try:
        hit = mixer.Sound(caminho_hit)
        hit.set_volume(VOLUME_HIT)

        print("Hit carregado com sucesso:")
        print(caminho_hit)

    except Exception as erro:
        hit = None

        print("Erro ao carregar hit:")
        print(caminho_hit)
        print(erro)


def tocar_hit():

    if not AUDIO_ATIVO:
        return

    carregar_hit()

    try:
        if hit is not None:
            hit.play()

    except Exception as erro:
        print("Erro ao tocar hit:", erro)


# ======================
# MUSICA DOS MENUS
# ======================

def tocar_musica_menu():

    global musica_menu_tocando

    if not AUDIO_ATIVO:
        return

    if musica_menu_tocando:
        return

    caminho_musica = encontrar_arquivo(ARQUIVOS_MUSICA_MENU)

    if caminho_musica is None:
        return

    try:
        mixer.music.load(caminho_musica)
        mixer.music.set_volume(VOLUME_MUSICA_MENU)
        mixer.music.play(-1)

        musica_menu_tocando = True

        print("Musica dos menus tocando:")
        print(caminho_musica)

    except Exception as erro:
        musica_menu_tocando = False

        print("Erro ao tocar musica dos menus:")
        print(caminho_musica)
        print(erro)


def parar_musica_menu():

    global musica_menu_tocando

    if not AUDIO_ATIVO:
        return

    if not musica_menu_tocando:
        return

    try:
        mixer.music.stop()

    except Exception as erro:
        print("Erro ao parar musica dos menus:", erro)

    musica_menu_tocando = False


# ======================
# COMPATIBILIDADE COM NOMES ANTIGOS
# ======================

def tocar_musica_jogo():

    tocar_musica_menu()


def parar_musica_jogo():

    parar_musica_menu()


def pausar_musica_jogo():

    parar_musica_menu()


def continuar_musica_jogo():

    tocar_musica_menu()


# ======================
# MOTOR DO CARRO
# ======================

def carregar_motor():

    global motor

    if not AUDIO_ATIVO:
        return

    if motor is not None:
        return

    caminho_motor = encontrar_arquivo(ARQUIVOS_MOTOR)

    if caminho_motor is None:
        return

    try:
        motor = mixer.Sound(caminho_motor)
        motor.set_volume(VOLUME_MOTOR)

        print("Motor carregado com sucesso:")
        print(caminho_motor)

    except Exception as erro:
        motor = None

        print("Erro ao carregar motor:")
        print(caminho_motor)
        print(erro)


def tocar_motor():

    global motor_tocando

    if not AUDIO_ATIVO:
        return

    if motor_tocando:
        return

    carregar_motor()

    try:
        if motor is not None:
            motor.play(-1)
            motor_tocando = True

    except Exception as erro:
        motor_tocando = False
        print("Erro ao tocar motor:", erro)


def parar_motor():

    global motor_tocando

    if not AUDIO_ATIVO:
        return

    if not motor_tocando:
        return

    try:
        if motor is not None:
            motor.stop()

    except Exception as erro:
        print("Erro ao parar motor:", erro)

    motor_tocando = False


def atualizar_motor(carro_andando):

    if carro_andando:
        tocar_motor()
    else:
        parar_motor()