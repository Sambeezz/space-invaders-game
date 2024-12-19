import pygame 
from pygame.sprite import Sprite 

class Bullet(Sprite):
    def __init__(self, polly):
        super().__init__()
        self.screen = polly.screen
        self.settings = polly.settings
        self.image = pygame.image.load('images/bullet.png')
        self.rect = self.image.get_rect()
        
        self.rect.midright = polly.ship.rect.midright
        
        self.x = float(self.rect.x)
        
    def update(self):
        self.x += self.settings.bullet_speed
        self.rect.x = self.x
        
    def draw_bullet(self):
        self.screen.blit(self.image, self.rect)
        