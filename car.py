from sprites import *
from keys import *
import fundo

# posição inicial
car.x = (1000 - car.width) / 2
car.y = 800 - car.height + 10

# velocidade lateral
velocidade_carro = 400

# piscar
pisca_timer = 0
intervalo_pisca = 0.12


def mover_carro(dt):

    global pisca_timer

    # esquerda
    if pressionada(LEFT):
        car.x -= velocidade_carro * dt

    # direita
    if pressionada(RIGHT):
        car.x += velocidade_carro * dt

    # limites
    if car.x < 0:
        car.x = 0

    if car.x > 1000 - car.width:
        car.x = 1000 - car.width

    # controla timer do pisca
    if fundo.velocidade_fundo < 300:
        pisca_timer += dt
    else:
        pisca_timer = 0


def desenhar_carro():

    # pisca enquanto velocidade reduzida
    if fundo.velocidade_fundo < 300:

        if int(pisca_timer / intervalo_pisca) % 2 == 0:
            car.draw()

    else:
        car.draw()