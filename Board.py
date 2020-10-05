import pygame, sys
from pygame.locals import *
import random

token_white_off = 7
token_black_off = 7
token_white_play = 0
token_black_play = 0
token_white_win = 0


#iniciar pygame
pygame.init()

pygame.font.init()
fuente = pygame.font.Font(None, 50)



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
ima23 = pygame.image.load("Imagenes/23.png")
ima22 = pygame.image.load("Imagenes/22.png")
ima21 = pygame.image.load("Imagenes/21.png")
ima20 = pygame.image.load("Imagenes/20.png")
ima10 = pygame.image.load("Imagenes/10.png")
ima11 = pygame.image.load("Imagenes/11.png")
ima12 = pygame.image.load("Imagenes/12.png")
ima13 = pygame.image.load("Imagenes/13.png")
ima14 = pygame.image.load("Imagenes/14.png")
ima15 = pygame.image.load("Imagenes/15.png")
ima16 = pygame.image.load("Imagenes/16.png")
ima17 = pygame.image.load("Imagenes/17.png")
ima27 = pygame.image.load("Imagenes/27.png")
ima26 = pygame.image.load("Imagenes/26.png")
win_w = pygame.image.load("Imagenes/win_white_fond.png")

#coordenadas para fondo del tablero
x,y = 0,0


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
    board_win.blit(dice2,(600,500))
    
   
    #board_win.blit(win_w,(575,420))
    

    global token_white_off
    global token_black_off
    global token_white_win

    
    
    texto1 = fuente.render('Win:', 1, (0, 0, 0))
    
    pygame.display.flip()
    
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
  
                print(mouse_x,mouse_y)
                if mouse_x >= 66 and mouse_x <= 138:
                    print("aqui x")
                    if mouse_y >= 228 and mouse_y <= 284:
                        print("aqui y")
                        

   
                #si se presionan los datos
                if mouse_x >= 600 and mouse_x <= 800:
                    if mouse_y >= 500 and mouse_y <= 600:
                        num = random.randint(1,4)
                        if num == 1:
                            board_win.blit(dice_fond,(597,497))
                            board_win.blit(dice1,(600,500))
                            mov(board_win, num)
                            board_win.blit(texto1, (610, 420))
                            texto = fuente.render(str(token_white_win), 1, (0, 0, 0))
                            board_win.blit(texto, (700, 423))
                            if token_white_win == 7:
                                 t = fuente.render("GANASTE!!!!!", 1, (255, 255, 0))
                                 board_win.blit(t, (300, 245))
                                 
                                     
                        elif num == 2:
                            board_win.blit(dice_fond,(597,497))
                            board_win.blit(dice2,(600,500))
                            mov(board_win, num)
                            board_win.blit(texto1, (610, 420))
                            texto = fuente.render(str(token_white_win), 1, (0, 0, 0))
                            board_win.blit(texto, (700, 423))
                            if token_white_win == 7:
                                 t = fuente.render("GANASTE!!!!!", 1, (255, 255, 0))
                                 board_win.blit(t, (305, 245))
                                 break
                                
                        elif num == 3:
                            board_win.blit(dice_fond,(597,497))
                            board_win.blit(dice3,(600,500))
                            mov(board_win, num)
                            board_win.blit(texto1, (610, 420))
                            texto = fuente.render(str(token_white_win), 1, (0, 0, 0))
                            board_win.blit(texto, (700, 423))
                            if token_white_win == 7:
                                 t = fuente.render("GANASTE!!!!!", 1, (255, 255, 0))
                                 board_win.blit(t, (305, 245))
                                 break
                                
                        elif num == 4:
                            board_win.blit(dice_fond,(597,497))
                            board_win.blit(dice4,(600,500))
                            mov(board_win, num)
                            board_win.blit(texto1, (610, 420))
                            texto = fuente.render(str(token_white_win), 1, (0, 0, 0))
                            board_win.blit(texto, (700, 423))
                            if token_white_win == 7:
                                 t = fuente.render("GANASTE!!!!!", 1, (255, 255, 0))
                                 board_win.blit(t, (305, 245))
                                 break
                        
        pygame.display.update()

    


def mov(board_win, num):
    global token_white_off
    global token_white_play
    global token_black_play
    global token_white_win
    
    flag = True
    while flag:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()    
            if event.type == MOUSEBUTTONUP:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                
#---------------para casilla de salida-------------------------------------------------------------------
                if mouse_x >= 425  and mouse_x <= 474 and num == 1:
                    if mouse_y >= 360 and mouse_y <= 400 :
                        for i in range(len(ma)):
                            for j in range(len(ma[i])):
                                if ma[2][3] == 0:#casilla vacia
                                        ma[2][3] = 3
                                        matriz(ma, board_win, 95, 97)
                                        if token_white_off != 0:
                                            token_white_off -= 1
                                            token_white_play += 1
                                        flag = False               
                elif mouse_x >= 425  and mouse_x <= 474 and num == 2:
                    if mouse_y >= 360 and mouse_y <= 400 :
                        for i in range(len(ma)):
                            for j in range(len(ma[i])):
                                if ma[2][2] == 0:#casilla vacia
                                        ma[2][2] = 3
                                        matriz(ma, board_win, 95, 97)
                                        if token_white_off != 0:
                                            token_white_off -= 1
                                            token_white_play += 1
                                        flag = False              
                elif mouse_x >= 425  and mouse_x <= 474 and num == 3:
                    if mouse_y >= 360 and mouse_y <= 400 :
                        for i in range(len(ma)):
                            for j in range(len(ma[i])):
                                if ma[2][1] == 0:
                                        ma[2][1] = 3
                                        matriz(ma, board_win, 95, 97)
                                        if token_white_off != 0:
                                            token_white_off -= 1
                                            token_white_play += 1
                                        flag = False
                elif mouse_x >= 425  and mouse_x <= 474 and num == 4:
                    if mouse_y >= 360 and mouse_y <= 400 :
                        for i in range(len(ma)):
                            for j in range(len(ma[i])):
                                if ma[2][0] == 0:#casilla vacia
                                        ma[2][0] = 3
                                        matriz(ma, board_win, 95, 97)
                                        if token_white_off != 0:
                                            token_white_off -= 1
                                            token_white_play += 1
                                        flag = False
                                    
#---------------casilla 1-----------------------------------------------------------------
                elif mouse_x >= 310  and mouse_x <= 390 and num == 1:
                    if mouse_y >= 300 and mouse_y <= 354:
                        if ma[2][3] == 3:
                            for i in range(len(ma)):
                                for j in range(len(ma[i])):
                                    if ma[2][2] == 0:#casilla vacia
                                        ma[2][3] = 0
                                        ma[2][2] = 3
                                        board_win.blit(ima23,(324,304))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                elif mouse_x >= 310  and mouse_x <= 390 and num == 2:
                    if mouse_y >= 300 and mouse_y <= 354 :
                        if ma[2][3] == 3:
                            for i in range(len(ma)):
                                for j in range(len(ma[i])):
                                    if ma[2][1] == 0:#casilla vacia
                                        ma[2][3] = 0
                                        ma[2][1] = 3
                                        board_win.blit(ima23,(324,304))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                elif mouse_x >= 310  and mouse_x <= 390 and num == 3:
                    if mouse_y >= 300 and mouse_y <= 354 :
                        if ma[2][3] == 3:
                            for i in range(len(ma)):
                                for j in range(len(ma[i])):
                                    if ma[2][0] == 0:#casilla vacia
                                        ma[2][3] = 0
                                        ma[2][0] = 3
                                        board_win.blit(ima23,(324,304))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                elif mouse_x >= 310  and mouse_x <= 390 and num == 4:
                    if mouse_y >= 300 and mouse_y <= 354 :
                        if ma[2][3] == 3:
                            for i in range(len(ma)):
                                for j in range(len(ma[i])):
                                    if ma[1][0] == 0:#casilla vacia
                                        ma[2][3] = 0
                                        ma[1][0] = 3
                                        board_win.blit(ima23,(324,304))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                                    elif ma[1][0] == 2:#casilla ocupada por oponente
                                        ma[2][3] = 0
                                        ma[1][0] = 3
                                        token_black_play -= 1
                                        token_black_off += 1
                                        board_win.blit(ima23,(324,304))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                                        

#---------------casilla 2--------------------------------------------------------------------------
                elif mouse_x >= 232 and mouse_x <= 298 and num == 1: 
                    if mouse_y >= 294 and mouse_y <= 353:
                        if ma[2][2] == 3:
                            for i in range(len(ma)):
                                for j in range(len(ma[i])):
                                    if ma[2][1] == 0:#casilla vacia
                                        ma[2][2] = 0
                                        ma[2][1] = 3
                                        board_win.blit(ima22,(235,292))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                elif mouse_x >= 232 and mouse_x <= 298 and num == 2: 
                    if mouse_y >= 294 and mouse_y <= 353:
                        if ma[2][2] == 3:
                            for i in range(len(ma)):
                                for j in range(len(ma[i])):
                                    if ma[2][0] == 0:#casilla vacia
                                        ma[2][2] = 0
                                        ma[2][0] = 3
                                        board_win.blit(ima22,(235,292))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                elif mouse_x >= 232 and mouse_x <= 298 and num == 3: 
                    if mouse_y >= 294 and mouse_y <= 353:
                        if ma[2][2] == 3:
                            for i in range(len(ma)):
                                for j in range(len(ma[i])):
                                    if ma[1][0] == 0:#casilla vacia
                                        ma[2][2] = 0
                                        ma[1][0] = 3
                                        board_win.blit(ima22,(235,292))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                                    elif ma[1][0] == 2:#casilla ocupada por oponente
                                        ma[2][2] = 0
                                        ma[1][0] = 3
                                        token_black_play -=1
                                        token_black_off += 1
                                        board_win.blit(ima22,(235,292))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                elif mouse_x >= 232 and mouse_x <= 298 and num == 4: 
                    if mouse_y >= 294 and mouse_y <= 353:
                        if ma[2][2] == 3:
                            for i in range(len(ma)):
                                for j in range(len(ma[i])):
                                    if ma[1][1] == 0:#casilla vacia
                                        ma[2][2] = 0
                                        ma[1][1] = 3
                                        board_win.blit(ima22,(235,292))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                                    elif ma[1][1] == 2:#casilla ocupada por oponente
                                        ma[2][2] = 0
                                        ma[1][1] = 3
                                        token_black_play -= 1
                                        token_black_off += 1
                                        board_win.blit(ima22,(235,292))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                                        
#---------------#casilla 3--------------------------------------------------------------------------
                elif mouse_x >= 147 and mouse_x <= 208 and num == 1:
                    if mouse_y >= 295 and mouse_y <= 356:
                        if ma[2][1] == 3:
                            for i in range(len(ma)):
                                for j in range(len(ma[i])):
                                    if ma[2][0] == 0:#casilla vacia
                                        ma[2][1] = 0
                                        ma[2][0] = 3
                                        board_win.blit(ima21,(146,299))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                elif mouse_x >= 147 and mouse_x <= 208 and num == 2:
                    if mouse_y >= 295 and mouse_y <= 356:
                        if ma[2][1] == 3:
                            for i in range(len(ma)):
                                for j in range(len(ma[i])):
                                    if ma[1][0] == 0:#casilla vacia
                                        ma[2][1] = 0
                                        ma[1][0] = 3
                                        board_win.blit(ima21,(146,299))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                                    elif ma[1][0] == 2:#casilla ocupada por oponente
                                        ma[2][1] = 0
                                        ma[1][0] = 3
                                        token_black_play -= 1
                                        token_black_off += 1
                                        board_win.blit(ima21,(146,299))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                elif mouse_x >= 147 and mouse_x <= 208 and num == 3:
                    if mouse_y >= 295 and mouse_y <= 356:
                        if ma[2][1] == 3:
                            for i in range(len(ma)):
                                for j in range(len(ma[i])):
                                    if ma[1][1] == 0:#casilla vacia
                                        ma[2][1] = 0
                                        ma[1][1] = 3
                                        board_win.blit(ima21,(146,299))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                                    elif ma[1][1] == 2:#casilla ocupada por oponente
                                        ma[2][1] = 0
                                        ma[1][1] = 3
                                        token_black_play -= 1
                                        token_black_off += 1
                                        board_win.blit(ima21,(146,299))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                elif mouse_x >= 147 and mouse_x <= 208 and num == 4:
                    if mouse_y >= 295 and mouse_y <= 356:
                        if ma[2][1] == 3:
                            for i in range(len(ma)):
                                for j in range(len(ma[i])):
                                    if ma[1][2] == 0:#casilla vacia
                                        ma[2][1] = 0
                                        ma[1][2] = 3
                                        board_win.blit(ima21,(146,299))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                                    elif ma[1][2] == 2:#casilla ocupada por oponente
                                        ma[2][1] = 0
                                        ma[1][2] = 3
                                        token_black_play -= 1
                                        token_black_off += 1
                                        board_win.blit(ima21,(146,299))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False

#---------------#casilla 4--------------------------------------------------------------------------
                elif mouse_x >= 46 and mouse_x <= 124 and num == 1:
                    if mouse_y >= 297 and mouse_y <= 356:
                        if ma[2][0] == 3:
                            for i in range(len(ma)):
                                for j in range(len(ma[i])):
                                    if ma[1][0] == 0:#casilla vacia
                                        ma[2][0] = 0
                                        ma[1][0] = 3
                                        board_win.blit(ima20,(56,299))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                                    elif ma[1][0] == 2:#casilla ocupada por oponente
                                        ma[2][0] = 0
                                        ma[1][0] = 3
                                        token_black_play -= 1
                                        token_black_off += 1
                                        board_win.blit(ima20,(56,299))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                elif mouse_x >= 46 and mouse_x <= 124 and num == 2:
                    if mouse_y >= 297 and mouse_y <= 356:
                        if ma[2][0] == 3:
                            for i in range(len(ma)):
                                for j in range(len(ma[i])):
                                    if ma[1][1] == 0:#casilla vacia
                                        ma[2][0] = 0
                                        ma[1][1] = 3
                                        board_win.blit(ima20,(56,299))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                                    elif ma[1][1] == 2:#casilla ocupada por oponente
                                        ma[2][0] = 0
                                        ma[1][1] = 3
                                        token_black_play -= 1
                                        token_black_off += 1
                                        board_win.blit(ima20,(56,299))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                elif mouse_x >= 46 and mouse_x <= 124 and num == 3:
                    if mouse_y >= 297 and mouse_y <= 356:
                        if ma[2][0] == 3:
                            for i in range(len(ma)):
                                for j in range(len(ma[i])):
                                    if ma[1][2] == 0:#casilla vacia
                                        ma[2][0] = 0
                                        ma[1][2] = 3
                                        board_win.blit(ima20,(56,299))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                                    elif ma[1][2] == 2:#casilla ocupada por oponente
                                        ma[2][0] = 0
                                        ma[1][2] = 3
                                        token_black_play -= 1
                                        token_black_off += 1
                                        board_win.blit(ima21,(146,299))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                elif mouse_x >= 46 and mouse_x <= 124 and num == 4:
                    if mouse_y >= 297 and mouse_y <= 356:
                        if ma[2][0] == 3:
                            for i in range(len(ma)):
                                for j in range(len(ma[i])):
                                    if ma[1][3] == 0:#casilla vacia
                                        ma[2][0] = 0
                                        ma[1][3] = 3
                                        board_win.blit(ima20,(56,299))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                                        

#---------------#casilla 5--------------------------------------------------------------------------
                if mouse_x >= 66 and mouse_x <= 138 and num == 1:
                    if mouse_y >= 228 and mouse_y <= 284:
                        print(11111)
                        if ma[1][0] == 3:
                            for i in range(len(ma)):
                                for j in range(len(ma[i])):
                                    if ma[1][1] == 0:#casilla vacia
                                        ma[1][0] = 0
                                        ma[1][1] = 3
                                        board_win.blit(ima10,(74,230))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                                    elif ma[1][1] == 2:#casilla ocupada por oponente
                                        ma[1][0] = 0
                                        ma[1][1] = 3
                                        token_black_play -= 1
                                        token_black_off += 1
                                        board_win.blit(ima10,(74,230))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                elif mouse_x >= 66 and mouse_x <= 138 and num == 2:
                    if mouse_y >= 228 and mouse_y <= 284:
                        if ma[1][0] == 3:
                            for i in range(len(ma)):
                                for j in range(len(ma[i])):
                                    if ma[1][2] == 0:#casilla vacia
                                        ma[1][0] = 0
                                        ma[1][2] = 3
                                        board_win.blit(ima10,(74,230))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                                    elif ma[1][2] == 2:#casilla ocupada por oponente
                                        ma[1][0] = 0
                                        ma[1][2] = 3
                                        token_black_play -= 1
                                        token_black_off += 1
                                        board_win.blit(ima10,(74,230))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                elif mouse_x >= 66 and mouse_x <= 138 and num == 3:
                    if mouse_y >= 228 and mouse_y <= 284:
                        if ma[1][0] == 3:
                            for i in range(len(ma)):
                                for j in range(len(ma[i])):
                                    if ma[1][3] == 0:#casilla vacia
                                        ma[1][0] = 0
                                        ma[1][3] = 3
                                        board_win.blit(ima10,(74,230))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                                    
                elif mouse_x >= 66 and mouse_x <= 138 and num == 4:
                    if mouse_y >= 228 and mouse_y <= 284:
                        if ma[1][0] == 3:
                            for i in range(len(ma)):
                                for j in range(len(ma[i])):
                                    if ma[1][4] == 0:#casilla vacia
                                        ma[1][0] = 0
                                        ma[1][4] = 3
                                        board_win.blit(ima10,(74,230))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                                    elif ma[1][4] == 2:#casilla ocupada por oponente
                                        ma[1][0] = 0
                                        ma[1][4] = 3
                                        token_black_play -= 1
                                        token_black_off += 1
                                        board_win.blit(ima10,(74,230))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False

#---------------#casilla 6--------------------------------------------------------------------------
                if mouse_x >= 153 and mouse_x <= 224 and num == 1:
                    if mouse_y >= 228 and mouse_y <= 285:
                        if ma[1][1] == 3:
                            for i in range(len(ma)):
                                for j in range(len(ma[i])):
                                    if ma[1][2] == 0:#casilla vacia
                                        ma[1][1] = 0
                                        ma[1][2] = 3
                                        board_win.blit(ima11,(158, 231))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                                    elif ma[1][2] == 2:#casilla ocupada por oponente
                                        ma[1][1] = 0
                                        ma[1][2] = 3
                                        token_black_play -= 1
                                        token_black_off += 1
                                        board_win.blit(ima11,(158, 231))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                elif mouse_x >= 153 and mouse_x <= 224 and num == 2:
                    if mouse_y >= 228 and mouse_y <= 285:
                        if ma[1][1] == 3:
                            for i in range(len(ma)):
                                for j in range(len(ma[i])):
                                    if ma[1][3] == 0:#casilla vacia
                                        ma[1][1] = 0
                                        ma[1][3] = 3
                                        board_win.blit(ima11,(158, 231))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                elif mouse_x >= 153 and mouse_x <= 224 and num == 3:
                    if mouse_y >= 228 and mouse_y <= 285:
                        if ma[1][1] == 3:
                            for i in range(len(ma)):
                                for j in range(len(ma[i])):
                                    if ma[1][4] == 0:#casilla vacia
                                        ma[1][1] = 0
                                        ma[1][4] = 3
                                        board_win.blit(ima11,(158, 231))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                                    elif ma[1][4] == 2:#casilla ocupada por oponente
                                        ma[1][1] = 0
                                        ma[1][4] = 3
                                        token_black_play -= 1
                                        token_black_off += 1
                                        board_win.blit(ima11,(158, 231))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                                    
                elif mouse_x >= 153 and mouse_x <= 224 and num == 4:
                    if mouse_y >= 228 and mouse_y <= 285:
                        if ma[1][1] == 3:
                            for i in range(len(ma)):
                                for j in range(len(ma[i])):
                                    if ma[1][5] == 0:#casilla vacia
                                        ma[1][1] = 0
                                        ma[1][5] = 3
                                        board_win.blit(ima11,(158, 231))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                                    elif ma[1][5] == 2:#casilla ocupada por oponente
                                        ma[1][1] = 0
                                        ma[1][5] = 3
                                        token_black_play -= 1
                                        token_black_off += 1
                                        board_win.blit(ima11,(158, 231))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False

#---------------#casilla 7--------------------------------------------------------------------------
                if mouse_x >= 238 and mouse_x <= 307 and num == 1:
                    if mouse_y >= 230 and mouse_y <= 283:
                        if ma[1][2] == 3: 
                            for i in range(len(ma)):
                                for j in range(len(ma[i])):
                                    if ma[1][3] == 0:#casilla vacia
                                        ma[1][2] = 0
                                        ma[1][3] = 3
                                        board_win.blit(ima12,(240, 233))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                elif mouse_x >= 238 and mouse_x <= 307 and num == 2:
                    if mouse_y >= 230 and mouse_y <= 283:
                        if ma[1][2] == 3:
                            for i in range(len(ma)):
                                for j in range(len(ma[i])):
                                    if ma[1][4] == 0:#casilla vacia
                                        ma[1][2] = 0
                                        ma[1][4] = 3
                                        board_win.blit(ima12,(240, 233))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                                    elif ma[1][4] == 2:# casilla ocupada por oponente
                                        ma[1][2] = 0
                                        ma[1][4] = 3
                                        token_black_play -= 1
                                        token_black_off += 1
                                        board_win.blit(ima12,(240, 233))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                elif mouse_x >= 238 and mouse_x <= 307 and num == 3:
                    if mouse_y >= 230 and mouse_y <= 283:
                        if ma[1][2] == 3:
                            for i in range(len(ma)):
                                for j in range(len(ma[i])):
                                    if ma[1][5] == 0:#casilla vacia
                                        ma[1][2] = 0
                                        ma[1][5] = 3
                                        board_win.blit(ima12,(240, 233))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                                    elif ma[1][5] == 2:# casilla ocupada por oponente
                                        ma[1][2] = 0
                                        ma[1][5] = 3
                                        token_black_play -= 1
                                        token_black_off += 1
                                        board_win.blit(ima12,(240, 233))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                                    
                elif mouse_x >= 238 and mouse_x <= 307 and num == 4:
                    if mouse_y >= 230 and mouse_y <= 283:
                        if ma[1][2] == 3:
                            for i in range(len(ma)):
                                for j in range(len(ma[i])):
                                    if ma[1][6] == 0:#casilla vacia
                                        ma[1][2] = 0
                                        ma[1][6] = 3
                                        board_win.blit(ima12,(240, 233))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                                    elif ma[1][6] == 2: # casilla ocupada por oponente
                                        ma[1][2] = 0
                                        ma[1][6] = 3
                                        token_black_play -= 1
                                        token_black_off += 1
                                        board_win.blit(ima12,(240, 233))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False

#---------------#casilla 8--------------------------------------------------------------------------
                if mouse_x >= 324 and mouse_x <= 393 and num == 1:
                    if mouse_y >= 231 and mouse_y <= 285:
                        if ma[1][3] == 3: 
                            for i in range(len(ma)):
                                for j in range(len(ma[i])):
                                    if ma[1][4] == 0:# casilla vacia
                                        ma[1][3] = 0
                                        ma[1][4] = 3
                                        board_win.blit(ima13,(325, 237))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                                    elif ma[1][4] == 2:# casilla ocupada por oponente
                                        ma[1][3] = 0
                                        ma[1][4] = 3
                                        token_black_play -= 1
                                        token_black_off += 1
                                        board_win.blit(ima13,(325, 237))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                elif mouse_x >= 324 and mouse_x <= 393 and num == 2:
                    if mouse_y >= 231 and mouse_y <= 285:
                        if ma[1][3] == 3:
                            for i in range(len(ma)):
                                for j in range(len(ma[i])):
                                    if ma[1][5] == 0:#casilla vacia
                                        ma[1][3] = 0
                                        ma[1][5] = 3
                                        board_win.blit(ima13,(325, 237))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                                    elif ma[1][5] == 2:# casilla ocupada por oponente
                                        ma[1][3] = 0
                                        ma[1][5] = 3
                                        token_black_play -= 1
                                        token_black_off += 1
                                        board_win.blit(ima13,(325, 237))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                elif mouse_x >= 324 and mouse_x <= 393 and num == 3:
                    if mouse_y >= 231 and mouse_y <= 285:
                        if ma[1][3] == 3:
                            for i in range(len(ma)):
                                for j in range(len(ma[i])):
                                    if ma[1][6] == 0:#casilla vacia
                                        ma[1][3] = 0
                                        ma[1][6] = 3
                                        board_win.blit(ima13,(325, 237))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                                    elif ma[1][6] == 2:# casilla ocupada por oponente
                                        ma[1][3] = 0
                                        ma[1][6] = 3
                                        token_black_play -= 1
                                        token_black_off += 1
                                        board_win.blit(ima13,(325, 237))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                                    
                elif mouse_x >= 324 and mouse_x <= 393 and num == 4:
                    if mouse_y >= 231 and mouse_y <= 285:
                        if ma[1][3] == 3:
                            for i in range(len(ma)):
                                for j in range(len(ma[i])):
                                    if ma[1][7] == 0: #casilla vacia
                                        ma[1][3] = 0
                                        ma[1][7] = 3
                                        board_win.blit(ima13,(325, 237))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                                    elif ma[1][7] == 2: # casilla ocupada por oponente
                                        ma[1][3] = 0
                                        ma[1][7] = 3
                                        token_black_play -= 1
                                        token_black_off += 1
                                        board_win.blit(ima13,(325, 237))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False

#---------------#casilla 9--------------------------------------------------------------------------
                if mouse_x >= 408 and mouse_x <= 480 and num == 1:
                    if mouse_y >= 229 and mouse_y <= 283:
                        if ma[1][4] == 3: 
                            for i in range(len(ma)):
                                for j in range(len(ma[i])):
                                    if ma[1][5] == 0:# casilla vacia
                                        ma[1][4] = 0
                                        ma[1][5] = 3
                                        board_win.blit(ima14,(415, 236))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                                    elif ma[1][5] == 2:# casilla ocupada por oponente
                                        ma[1][4] = 0
                                        ma[1][5] = 3
                                        token_black_play -= 1
                                        token_black_off += 1
                                        board_win.blit(ima14,(415, 236))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                elif mouse_x >= 408 and mouse_x <= 480 and num == 2:
                    if mouse_y >= 229 and mouse_y <= 283:
                        if ma[1][4] == 3:
                            for i in range(len(ma)):
                                for j in range(len(ma[i])):
                                    if ma[1][6] == 0:#casilla vacia
                                        ma[1][4] = 0
                                        ma[1][6] = 3
                                        board_win.blit(ima14,(415, 236))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                                    elif ma[1][6] == 2:# casilla ocupada por oponente
                                        ma[1][4] = 0
                                        ma[1][6] = 3
                                        token_black_play -= 1
                                        token_black_off += 1
                                        board_win.blit(ima14,(415, 236))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                elif mouse_x >= 408 and mouse_x <= 480 and num == 3:
                    if mouse_y >= 229 and mouse_y <= 283:
                        if ma[1][4] == 3:
                            for i in range(len(ma)):
                                for j in range(len(ma[i])):
                                    if ma[1][7] == 0:#casilla vacia
                                        ma[1][4] = 0
                                        ma[1][7] = 3
                                        board_win.blit(ima14,(415, 236))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                                    elif ma[1][7] == 2:# casilla ocupada por oponente
                                        ma[1][4] = 0
                                        ma[1][7] = 3
                                        token_black_play -= 1
                                        token_black_off += 1
                                        board_win.blit(ima14,(415, 236))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                                    
                elif mouse_x >= 408 and mouse_x <= 480 and num == 4:
                    if mouse_y >= 229 and mouse_y <= 283:
                        if ma[1][4] == 3:
                            for i in range(len(ma)):
                                for j in range(len(ma[i])):
                                    if ma[2][7] == 0: #casilla vacia
                                        ma[1][4] = 0
                                        ma[2][7] = 3
                                        board_win.blit(ima14,(415, 236))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False

#---------------#casilla 10--------------------------------------------------------------------------
                if mouse_x >= 495 and mouse_x <= 565 and num == 1:
                    if mouse_y >= 231 and mouse_y <= 285:
                        if ma[1][5] == 3: 
                            for i in range(len(ma)):
                                for j in range(len(ma[i])):
                                    if ma[1][6] == 0:# casilla vacia
                                        ma[1][5] = 0
                                        ma[1][6] = 3
                                        board_win.blit(ima15,(494, 235))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                                    elif ma[1][6] == 2:# casilla ocupada por oponente
                                        ma[1][5] = 0
                                        ma[1][6] = 3
                                        token_black_play -= 1
                                        token_black_off += 1
                                        board_win.blit(ima15,(494, 235))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                elif mouse_x >= 495 and mouse_x <= 565 and num == 2:
                    if mouse_y >= 231 and mouse_y <= 285:
                        if ma[1][5] == 3:
                            for i in range(len(ma)):
                                for j in range(len(ma[i])):
                                    if ma[1][7] == 0:#casilla vacia
                                        ma[1][5] = 0
                                        ma[1][7] = 3
                                        board_win.blit(ima15,(494, 235))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                                    elif ma[1][7] == 2:# casilla ocupada por oponente
                                        ma[1][5] = 0
                                        ma[1][7] = 3
                                        token_black_play -= 1
                                        token_black_off += 1
                                        board_win.blit(ima15,(494, 235))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                elif mouse_x >= 495 and mouse_x <= 565 and num == 3:
                    if mouse_y >= 231 and mouse_y <= 285:
                        if ma[1][5] == 3:
                            for i in range(len(ma)):
                                for j in range(len(ma[i])):
                                    if ma[2][7] == 0:#casilla vacia
                                        ma[1][5] = 0
                                        ma[2][7] = 3
                                        board_win.blit(ima15,(494, 235))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                                    
                elif mouse_x >= 495 and mouse_x <= 565 and num == 4:
                    if mouse_y >= 231 and mouse_y <= 285:
                        if ma[1][5] == 3:
                            for i in range(len(ma)):
                                for j in range(len(ma[i])):
                                    if ma[2][6] == 0: #casilla vacia
                                        ma[1][5] = 0
                                        ma[2][6] = 3
                                        board_win.blit(ima15,(494, 235))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False

#---------------#casilla 11--------------------------------------------------------------------------
                if mouse_x >= 583 and mouse_x <= 653 and num == 1:
                    if mouse_y >= 231 and mouse_y <= 285:
                        if ma[1][6] == 3: 
                            for i in range(len(ma)):
                                for j in range(len(ma[i])):
                                    if ma[1][7] == 0:# casilla vacia
                                        ma[1][6] = 0
                                        ma[1][7] = 3
                                        board_win.blit(ima16,(584, 236))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                                    elif ma[1][7] == 2:# casilla ocupada por oponente
                                        ma[1][6] = 0
                                        ma[1][7] = 3
                                        token_black_play -= 1
                                        token_black_off += 1
                                        board_win.blit(ima16,(584, 236))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                elif mouse_x >= 583 and mouse_x <= 653 and num == 2:
                    if mouse_y >= 231 and mouse_y <= 285:
                        if ma[1][6] == 3:
                            for i in range(len(ma)):
                                for j in range(len(ma[i])):
                                    if ma[2][7] == 0:#casilla vacia
                                        ma[1][6] = 0
                                        ma[2][7] = 3
                                        board_win.blit(ima16,(584, 236))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                elif mouse_x >= 583 and mouse_x <= 653 and num == 3:
                    if mouse_y >= 231 and mouse_y <= 285:
                        if ma[1][6] == 3:
                            for i in range(len(ma)):
                                for j in range(len(ma[i])):
                                    if ma[2][6] == 0:#casilla vacia
                                        ma[1][6] = 0
                                        ma[2][6] = 3
                                        board_win.blit(ima16,(584, 236))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                                    
                elif mouse_x >= 583 and mouse_x <= 653 and num == 4:
                    if mouse_y >= 231 and mouse_y <= 285:
                        if ma[1][6] == 3:
                            ma[1][6] = 0
                            token_white_play -=1
                            token_white_win += 1
                            board_win.blit(ima16,(584, 236))
                            board_win.blit(win_w,(575,420))
                            matriz(ma, board_win, 95, 97)
                            flag = False

#---------------#casilla 12--------------------------------------------------------------------------
                if mouse_x >= 666 and mouse_x <= 735 and num == 1:
                    if mouse_y >= 232 and mouse_y <= 286:
                        if ma[1][7] == 3: 
                            for i in range(len(ma)):
                                for j in range(len(ma[i])):
                                    if ma[2][7] == 0:# casilla vacia
                                        ma[1][7] = 0
                                        ma[2][7] = 3
                                        board_win.blit(ima17,(671, 237))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                elif mouse_x >= 666 and mouse_x <= 735 and num == 2:
                    if mouse_y >= 232 and mouse_y <= 286:
                        if ma[1][7] == 3:
                            for i in range(len(ma)):
                                for j in range(len(ma[i])):
                                    if ma[2][6] == 0:#casilla vacia
                                        ma[1][7] = 0
                                        ma[2][6] = 3
                                        board_win.blit(ima17,(671, 237))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                elif mouse_x >= 666 and mouse_x <= 735 and num == 3:
                    if mouse_y >= 232 and mouse_y <= 286:
                        if ma[1][7] == 3:
                            ma[1][7] = 0
                            token_white_play -=1
                            token_white_win += 1
                            board_win.blit(ima17,(671, 237))
                            board_win.blit(win_w,(575,420))
                            matriz(ma, board_win, 95, 97)
                            flag = False

#---------------#casilla 13--------------------------------------------------------------------------
                if mouse_x >= 666 and mouse_x <= 735 and num == 1:
                    if mouse_y >= 301 and mouse_y <= 358:
                        if ma[2][7] == 3: 
                            for i in range(len(ma)):
                                for j in range(len(ma[i])):
                                    if ma[2][6] == 0:# casilla vacia
                                        ma[2][7] = 0
                                        ma[2][6] = 3
                                        board_win.blit(ima27,(682, 305))
                                        matriz(ma, board_win, 95, 97)
                                        flag = False
                elif mouse_x >= 666 and mouse_x <= 735 and num == 2:
                    if mouse_y >= 301 and mouse_y <= 358:
                        if ma[2][7] == 3:
                            ma[2][7] = 0
                            token_white_play -=1
                            token_white_win += 1
                            board_win.blit(ima27,(682, 305))
                            board_win.blit(win_w,(575,420))
                            matriz(ma, board_win, 95, 97)
                            flag = False
                                    
#---------------#casilla 14--------------------------------------------------------------------------
                if mouse_x >= 590 and mouse_x <= 664 and num == 1:
                    if mouse_y >= 300 and mouse_y <= 360:
                        if ma[2][6] == 3:
                            ma[2][6] = 0
                            token_white_play -=1
                            token_white_win += 1
                            board_win.blit(ima26,(584, 301))
                            board_win.blit(win_w,(575,420))
                            matriz(ma, board_win, 95, 97)
                            flag = False

                
                if mouse_x >= 600 and mouse_x <= 800:
                    if mouse_y >= 500 and mouse_y <= 600:
                        flag = False
        pygame.display.update()
                                               
#funcion para mostrar la ficha de los jugadores en el tablero
def matriz(m, c, x, y):
    for k in range(len(m)):
        y+=70
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
