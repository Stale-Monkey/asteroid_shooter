import pygame
from sys import *

class Ship(pygame.sprite.Sprite):
    def __init__(self, groups,):

        # 1. we have to init the parent class
        super().__init__(groups) 
        
        # We need a surface -> image
        self.image = pygame.image.load('../graphics/ship.png').convert_alpha()

        # We need a rect
        self.rect = self.image.get_rect(center = (window_width / 2, window_height / 2))

class Laser(pygame.sprite.Sprite):
    def __init__(self, groups, pos):

        super().__init__(groups)

        self.image = pygame.image.load('../graphics/laser.png').convert_alpha()

        self.rect = self.image.get_rect(midbottom = (pos.midtop))

# basic setup
pygame.init()
pygame.display.set_caption("Asteroid Shooter")
window_width, window_height = 1280, 720
display_surf = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()

# background
background_surf = pygame.image.load('../graphics/background.png').convert()

# sprite groups
spaceship_group = pygame.sprite.Group()
laser_group = pygame.sprite.Group()

# sprite creation
ship = Ship(spaceship_group)
laser = Laser(laser_group, ship.rect)

# game loop
while True:
   
   # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # delta time
    dt = clock.tick() / 1000

    # background
    display_surf.blit(background_surf, (0,0))

    # graphics
    spaceship_group.draw(display_surf)
    laser_group.draw(display_surf)

    # draw the frame
    pygame.display.update()