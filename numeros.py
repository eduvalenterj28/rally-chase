from PPlay.sprite import *

# ======================
# CONFIGURAÇÃO
# ======================

# antes era fixo e grande demais para 30x30
ESPACAMENTO = 24

# ======================
# DESENHAR TEXTO NUMÉRICO
# ======================

def desenhar_numero(texto, x, y):

    for caractere in str(texto):

        # ------------------
        # DÍGITOS
        # ------------------

        if caractere.isdigit():

            sprite = Sprite(
                f"sprites/{caractere}.png"
            )

            sprite.set_position(x, y)
            sprite.draw()

            x += ESPACAMENTO

        # ------------------
        # PORCENTAGEM
        # ------------------

        elif caractere == "%":

            sprite = Sprite(
                "sprites/porCento.png"
            )

            sprite.set_position(x, y)
            sprite.draw()

            x += 22  # menor que número para ficar mais compacto

        # ------------------
        # DOIS PONTOS
        # ------------------

        elif caractere == ":":

            # agora ocupa menos espaço visual
            x += 10

        # ------------------
        # ESPAÇO
        # ------------------

        elif caractere == " ":

            x += 12