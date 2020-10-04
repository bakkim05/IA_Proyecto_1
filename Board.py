import pygame, sys
from pygame.locals import *
import random

#iniciar pygame
pygame.init()

#cargar las imagenes a utilizar
image_board = pygame.image.load("Imagenes/board.png")
black = pygame.image.load("Imagenes/black.png")
no_black = pygame.image.load("Imagenes/no_black.png")
white = pygame.image.load("Imagenes/white.png")
no_white = pygame.image.load("Imagenes/no_white.png")
dice1 = pygame.image.load("Imagenes/dice1.png")
dice2 = pygame.image.load("Imagenes/dice2.png")
dice3 = pygame.image.load("Imagenes/dice3.png")
dice4 = pygame.image.load("Imagenes/dice4.png")
dice_fond = pygame.image.load("Imagenes/dice_fond.png")

#coordenadas para fondo del tablero
x,y = 0,0

#global contador de puntajes(negro, blanco)
#global fichas en juego


#matriz de prueba
ma=[[0,0,0,0,1,1,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,1,1,0,0]]

maxi=[[2,0,0,0,1,1,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,1,1,0,0]]

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

    token_white_off = 5
    token_black_off = 5
    
    #llamar funcion para mostar fichas de jugadores
    matriz(ma,board_win, 95, 97)

    while True:
        for event in pygame.event.get():
            #verificar si no han salido fichas
            if token_white_off !=0:
                board_win.blit(white,(430,360))
            else:
                board_win.blit(no_white,(413,350))
                
            if token_black_off !=0:
                board_win.blit(black,(420,160))
            else:
                board_win.blit(no_black,(413,153))
                
            #cerrar ventana 
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #si se cliclea
            if event.type == MOUSEBUTTONUP:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                #si se presionan los datos
                if mouse_x >= 600 and mouse_x <= 800:
                    if mouse_y >= 500 and mouse_y <= 600:
                        num = random.randint(1,4)
                        if num == 1:
                            board_win.blit(dice_fond,(597,497))
                            board_win.blit(dice1,(600,500))
                            mov(board_win, num)
                            if token_white_off != 0:
                                token_white_off -= 1
                        elif num == 2:
                            board_win.blit(dice_fond,(597,497))
                            board_win.blit(dice2,(600,500))
                            mov(board_win, num)
                            if token_white_off != 0:
                                token_white_off -= 1
                        elif num == 3:
                            board_win.blit(dice_fond,(597,497))
                            board_win.blit(dice3,(600,500))
                            mov(board_win, num)
                            if token_white_off != 0:
                                token_white_off -= 1
                        elif num == 4:
                            board_win.blit(dice_fond,(597,497))
                            board_win.blit(dice4,(600,500))
                            mov(board_win, num)
                            if token_white_off != 0:
                                token_white_off -= 1
                        
        pygame.display.update()



def mov(board_win, num):
    flag = True
    
    while flag:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == MOUSEBUTTONUP:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                
                if mouse_x >= 425  and mouse_x <= 474 and num == 1:
                    if mouse_y >= 360 and mouse_y <= 400 :
                        print(1)
                        for i in range(len(ma)):
                            for j in range(len(ma[i])):
                                if ma[2][3] == 0:
                                        ma[2][3] = 3
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                                else:
                                    flag = False
                                    
                elif mouse_x >= 425  and mouse_x <= 474 and num == 2:
                    if mouse_y >= 360 and mouse_y <= 400 :
                        for i in range(len(ma)):
                            for j in range(len(ma[i])):
                                if ma[2][2] == 0:
                                        ma[2][2] = 3
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                                else:
                                    flag = False
                                    
                elif mouse_x >= 425  and mouse_x <= 474 and num == 3:
                    if mouse_y >= 360 and mouse_y <= 400 :
                        for i in range(len(ma)):
                            for j in range(len(ma[i])):
                                if ma[2][1] == 0:
                                        ma[2][1] = 3
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                                else:
                                    flag = False

                elif mouse_x >= 425  and mouse_x <= 474 and num == 4:
                    if mouse_y >= 360 and mouse_y <= 400 :
                        for i in range(len(ma)):
                            for j in range(len(ma[i])):
                                if ma[2][0] == 0:
                                        ma[2][0] = 3
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                                else:
                                    flag = False
                                    
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
