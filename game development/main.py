# python -m  pygame.examples.aliens
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    pygame.display.flip()

pygame.init()

# TO INSTALL PIP RUN THE COMMAND BELOW:
# py -m pip install --upgrade pip

# C:\user\HP\AppData\Local\Program\Python\Python311\Scripts