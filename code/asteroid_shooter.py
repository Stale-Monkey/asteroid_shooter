import pygame
from sys import *
from random import randint, uniform

class Ship(pygame.sprite.Sprite):
    def __init__(self, groups, can_shoot, shoot_time):

        # 1. we have to init the parent class
        super().__init__(groups) 
        
        # We need a surface -> image
        self.image = pygame.image.load('../graphics/ship.png').convert_alpha()

        # We need a rect
        self.rect = self.image.get_rect(center = (window_width / 2, window_height / 2))

        self.can_shoot = can_shoot

        self.shoot_time = shoot_time
    
    def input_pos(self):
         pos = pygame.mouse.get_pos()
         self.rect.center = pos

    def laser_shoot(self):

        if pygame.mouse.get_pressed()[0] and self.can_shoot:
            print('shoot laser')

            self.can_shoot = False
            self.shoot_time = pygame.time.get_ticks()
            Laser(self.rect.midtop, laser_group)

    def laser_timer(self, duration = 500):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_time > duration:
                self.can_shoot = True

    def update(self):
            self.input_pos()
            self.laser_shoot()
            self.laser_timer()

class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, groups,):

        super().__init__(groups)

        self.image = pygame.image.load('../graphics/laser.png').convert_alpha()

        self.rect = self.image.get_rect(midbottom = pos)
        
        # float based position
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(0, -1)
        self.speed = 600

    def update(self):
        self.pos += self.direction * self.speed * dt
        self.rect.topleft = (round(self.pos.x),round(self.pos.y))

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.image = pygame.image.load('../graphics/meteor.png').convert_alpha()

    

        self.rect = self.image.get_rect(center = pos)

        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(uniform(-0.5, 0.5), +1)
        self.speed = randint(400, 600)

    def update(self):
        self.pos += self.direction * self.speed * dt
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))

class Score:
    def __init__(self):
        self.font = pygame.font.Font('../graphics/subatomic.ttf', 50)

    def display(self):
        score_text = f'Score: {pygame.time.get_ticks() // 1000}'
        text_surf = self.font.render(score_text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(midbottom = (window_width / 2, window_height - 80))
        display_surf.blit(text_surf, text_rect)
        pygame.draw.rect(display_surf, (255, 255, 255), text_rect.inflate(30, 30), width = 8, border_radius= 10)


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
asteroid_group = pygame.sprite.Group()

# asteroid timer
asteroid_timer = pygame.event.custom_type()
pygame.time.set_timer(asteroid_timer, 500)

# sprite creation
ship = Ship(spaceship_group, True, None)
score = Score()

# game loop
while True:
   
   # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == asteroid_timer:
            x_asteroid_pos = randint(-100, window_width + 100)
            y_asteroid_pos = randint(-100, -50)
            Asteroid((x_asteroid_pos, y_asteroid_pos), asteroid_group)
    
    # delta time
    dt = clock.tick() / 1000

    # background
    display_surf.blit(background_surf, (0,0))

    # update
    spaceship_group.update()
    laser_group.update()
    asteroid_group.update()

    # score
    score.display()

    # graphics
    spaceship_group.draw(display_surf)
    laser_group.draw(display_surf)
    asteroid_group.draw(display_surf)
  

    # draw the frame
    pygame.display.update()