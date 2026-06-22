from PPlay.sprite import *

# ======================
# CONFIGURAÇÃO
# ======================

ESPACAMENTO = 26

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

            sprite = Sprite("sprites/porCento.png")

            sprite.set_position(x, y)
            sprite.draw()

            x += sprite.width - 4

        # ------------------
        # DOIS PONTOS (LEVEMENTE MAIS ALTO)
        # ------------------

        elif caractere == ":":

            sprite = Sprite("sprites/2pontos.png")

            
            sprite.set_position(x, y - 3)

            sprite.draw()

            x += sprite.width

        # ------------------
        # ESPAÇO
        # ------------------

        elif caractere == " ":

            x += 14