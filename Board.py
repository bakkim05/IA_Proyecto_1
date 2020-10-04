import pygame, sys
from pygame.locals import *
import random

#iniciar pygame
pygame.init()

#cargar las imagenes a utilizar
image_board = pygame.image.load("Imagenes/board.png")
black = pygame.image.load("Imagenes/black.png")
white = pygame.image.load("Imagenes/white.png")
dice1 = pygame.image.load("Imagenes/dice1.png")
dice2 = pygame.image.load("Imagenes/dice2.png")
dice3 = pygame.image.load("Imagenes/dice3.png")
dice4 = pygame.image.load("Imagenes/dice4.png")
dice_fond = pygame.image.load("Imagenes/dice_fond.png")

#coordenadas para fondo del tablero
x,y = 0,0

#global contador de puntajes(negro, blanco)
#global fichas en juego
token_black_off=5
token_white_off=5

#matriz de prueba
ma=[[2,0,0,0,1,1,0,0],[0,0,0,0,0,0,0,0],[0,0,3,0,1,1,0,0]]

#matriz para verificar espacios especiales
matr=[[4,0,0,0,1,1,4,0],[0,0,0,4,0,0,0,0],[4,0,0,0,1,1,4,0]]

#verificar si es casilla especial
def veri_max(i,j):
    if matr[i][j] == 4:
        return True
    else:
        return False

#logica de interfaz tablero 
def board():
    #mostrar imagenes generales
    board_win = pygame.display.set_mode((800,600))
    pygame.display.set_caption("ROYAL GAME OF UR")
    board_win.blit(image_board,(0,0))
    board_win.blit(dice1,(600,500))
    
    #llamar funcion para mostar fichas de jugadores
    matriz(ma,board_win, 95, 97)
    
    #verificar si no han salido fichas
    if token_white_off !=0:
        board_win.blit(white,(430,360))
    if token_black_off !=0:
        board_win.blit(black,(420,160))
        
    while True:
        for event in pygame.event.get():
            #cerrar ventana 
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            #si se cliclea
            if event.type == MOUSEBUTTONUP:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                num = random.randint(1,4)
                if mouse_x >= 600 and mouse_x <= 800:
                    if mouse_y >= 500 and mouse_y <= 600:
                        if num == 1:
                            board_win.blit(dice_fond,(597,497))
                            board_win.blit(dice1,(600,500))
                        elif num == 2:
                            board_win.blit(dice_fond,(597,497))
                            board_win.blit(dice2,(600,500))
                        elif num == 3:
                            board_win.blit(dice_fond,(597,497))
                            board_win.blit(dice3,(600,500))
                        elif num == 4:
                            board_win.blit(dice_fond,(597,497))
                            board_win.blit(dice4,(600,500))
        pygame.display.update()


#funcion para mostrar la ficha de los jugadores en el tablero
def matriz(m, c, x, y):
    for k in range(len(m)):
        y+=68
        if k == 1:
            x=80
        elif k == 2:
            x=70
        for j in range(len(m[k])):
            if m[k][j] == 2:
                c.blit(black,(x,y))
                if k==2:
                    x += 90
                elif k==1:
                    x += 85
                else:
                    x+=80
            elif m[k][j] == 3:
                c.blit(white,(x,y))
                if k==2:
                    x += 90
                elif k==1:
                    x += 85
                else:
                    x+=80
            else:
                if k==2:
                    x += 90
                elif k==1:
                    x += 85
                else:
                    x+=80
