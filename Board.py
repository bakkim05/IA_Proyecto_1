import pygame, sys
from pygame.locals import *

pygame.init()
image_board = pygame.image.load("Imagenes/board.png")
x,y = 0,0

rec1 = pygame.Rect(95,170,50,50)

def board():
    board_win = pygame.display.set_mode((800,600))
    pygame.display.set_caption("ROYAL GAME OF UR")
    board_win.blit(image_board,(0,0))
    pygame.draw.rect(board_win,(255, 255, 255, 127),rec1)
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
