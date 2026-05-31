from keys import *
from window import *
from sprites import *


#posic incial
car.x = (1000 - car.width) / 2
car.y = 800 -car.height + 10

velCarro = 400

def mover_carro(dt):

    # esquerda
    if pressionada(LEFT):
        car.x -= velCarro * dt

    # direita
    if pressionada(RIGHT):
        car.x += velCarro * dt

    # limites da tela
    if car.x < 0:
        car.x = 0

    if car.x > 1000 - car.width:
        car.x = 1000 - car.width


def desenhar_carro():

    car.draw()