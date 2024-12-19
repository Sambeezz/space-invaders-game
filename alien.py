from random import randint

import pygame 
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, polly):
        super().__init__()
        self.screen = polly.screen
        self.settings = polly.settings 
        
        self.image = pygame.image.load('images/alien.bmp')
        self.image = pygame.transform.scale(self.image, (100, 140))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        
        self.rect.left = self.screen.get_rect().right
        
        alien_top_max = self.settings.screen_height - self.rect.height
        self.rect.top = randint(0, alien_top_max)
        
        self.x = float(self.rect.x)

    def update(self):
        self.x -= self.settings.alien_speed
        self.rect.x = self.x
        
        

  