from PPlay.keyboard import *

teclado = Keyboard()

# movimentação
LEFT = "LEFT"
RIGHT = "RIGHT"
UP = "UP"
DOWN = "DOWN"

# ações
SPACE = "SPACE"
ENTER = "ENTER"
ESC = "ESC"

def pressionada(tecla):
    return teclado.key_pressed(tecla)