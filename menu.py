from sprites import *
from keys import *

MENU = 0
TELA_FASE = 1
JOGO = 2
FIM = 3

estado = MENU


def atualizar_menu():

    global estado

    if pressionada(SPACE):

        estado = TELA_FASE


def desenhar_menu():

    menuInicial.draw()