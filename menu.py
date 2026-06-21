from sprites import *
from keys import *

MENU = 0
JOGO = 1
FIM = 2

estado = MENU


def atualizar_menu():

    global estado

    if pressionada(SPACE):
        estado = JOGO


def desenhar_menu():

    menuInicial.draw()