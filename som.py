import os
import pygame

# ============================================================
# CONFIGURAÇÕES DE ÁUDIO
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PASTA_MUSICA = os.path.join(BASE_DIR, "musica")

ARQUIVO_CLICK = os.path.join(PASTA_MUSICA, "click.wav")
ARQUIVO_MUSICA_JOGO = os.path.join(PASTA_MUSICA, "musicaJogo.wav")
ARQUIVO_MOTOR = os.path.join(PASTA_MUSICA, "motor.wav")

VOLUME_CLICK = 0.7
VOLUME_MUSICA = 0.35
VOLUME_MOTOR = 0.35

som_click = None
som_motor = None
canal_motor = None

audio_inicializado = False
musica_iniciada = False


# ============================================================
# INICIALIZAÇÃO
# ============================================================

def inicializar_audio():
    global som_click, som_motor, canal_motor, audio_inicializado

    if audio_inicializado:
        return

    try:
        if not pygame.mixer.get_init():
            pygame.mixer.init()

        pygame.mixer.set_num_channels(8)

        som_click = carregar_som(ARQUIVO_CLICK)
        som_motor = carregar_som(ARQUIVO_MOTOR)

        if som_click:
            som_click.set_volume(VOLUME_CLICK)

        if som_motor:
            som_motor.set_volume(VOLUME_MOTOR)

        canal_motor = pygame.mixer.Channel(1)

        audio_inicializado = True

    except Exception as erro:
        print("[ERRO] Não foi possível inicializar o áudio.")
        print(erro)


def carregar_som(caminho):
    if not os.path.exists(caminho):
        print(f"[AVISO] Arquivo de som não encontrado: {caminho}")
        return None

    try:
        return pygame.mixer.Sound(caminho)
    except Exception as erro:
        print(f"[ERRO] Não foi possível carregar o som: {caminho}")
        print(erro)
        return None


# ============================================================
# CLICK
# ============================================================

def tocar_click():
    inicializar_audio()

    if som_click:
        som_click.play()


# ============================================================
# MÚSICA DE FUNDO
# ============================================================

def iniciar_musica_jogo():
    global musica_iniciada

    inicializar_audio()

    if musica_iniciada:
        return

    if not os.path.exists(ARQUIVO_MUSICA_JOGO):
        print(f"[AVISO] Música do jogo não encontrada: {ARQUIVO_MUSICA_JOGO}")
        return

    try:
        pygame.mixer.music.load(ARQUIVO_MUSICA_JOGO)
        pygame.mixer.music.set_volume(VOLUME_MUSICA)
        pygame.mixer.music.play(-1)
        musica_iniciada = True

    except Exception as erro:
        print("[ERRO] Não foi possível iniciar a música do jogo.")
        print(erro)


def parar_musica_jogo():
    global musica_iniciada

    if pygame.mixer.get_init():
        pygame.mixer.music.stop()

    musica_iniciada = False


def pausar_musica_jogo():
    if pygame.mixer.get_init():
        pygame.mixer.music.pause()


def retomar_musica_jogo():
    if pygame.mixer.get_init():
        pygame.mixer.music.unpause()


# ============================================================
# SOM DO MOTOR
# ============================================================

def tocar_motor():
    inicializar_audio()

    if not som_motor or not canal_motor:
        return

    if not canal_motor.get_busy():
        canal_motor.play(som_motor, loops=-1)


def parar_motor():
    if canal_motor and canal_motor.get_busy():
        canal_motor.stop()


def atualizar_som_motor(carro_andando, jogo_pausado=False, tela_atual="jogo"):
    motor_deve_tocar = (
        carro_andando
        and not jogo_pausado
        and tela_atual == "jogo"
    )

    if motor_deve_tocar:
        tocar_motor()
    else:
        parar_motor()


# ============================================================
# PAUSE / RETOMADA GERAL
# ============================================================

def pausar_audio_jogo():
    pausar_musica_jogo()
    parar_motor()


def retomar_audio_jogo():
    retomar_musica_jogo()


def parar_todos_os_sons():
    parar_motor()
    parar_musica_jogo()


# ============================================================
# FUNÇÕES DE COMPATIBILIDADE COM SEU CÓDIGO ATUAL
# ============================================================

def atualizar_motor(carro_andando, jogo_pausado=False, tela_atual="jogo"):
    atualizar_som_motor(
        carro_andando=carro_andando,
        jogo_pausado=jogo_pausado,
        tela_atual=tela_atual
    )


def tocar_musica_jogo():
    iniciar_musica_jogo()


def tocar_musica():
    iniciar_musica_jogo()


def parar_musica():
    parar_musica_jogo()


def pausar_musica():
    pausar_musica_jogo()


def retomar_musica():
    retomar_musica_jogo()