import pygame

# Initialize pygame
from Board import *


pygame.init()

screen_width = 800
screen_height = 600


# Screen creation
screen = pygame.display.set_mode((screen_width,screen_height))

#Title and Icon
pygame.display.set_caption("Royal Game of Ur")
icon = pygame.image.load("images/icon.png")
pygame.display.set_icon(icon)

#Load Images
Login_base = pygame.image.load("images/Login1.png")

Login_selected = pygame.image.load("images/Login2.png")

#Functions
def login_screen_unselected():
    screen.blit(Login_base,(0,0))

def login_screen_selected():
    screen.blit(Login_selected,(0,0))


# Game Loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           pygame.display.quit()
           running = False

    screen.fill((0,0,0)) #RGB Value
    login_screen_unselected()

    mouse_pos = pygame.mouse.get_pos()
    
    if (mouse_pos[0] >= 300 and mouse_pos[0] <=500 and mouse_pos[1] >= 400 and mouse_pos[1] <= 500):
        login_screen_selected()
        if (pygame.mouse.get_pressed()[0]):
            board()
            




    

    pygame.display.update()


pygame.quit()
quit()
