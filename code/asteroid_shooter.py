import pygame
from sys import *

# basic setup
pygame.init()
pygame.display.set_caption("Asteroid Shooter")
window_width, window_height = 1280, 720
display_surf = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()

# game loop
while True:
   
   # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # delta time
    dt = clock.tick() / 1000

    # draw the frame
    pygame.display.update()