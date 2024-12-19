import pygame 

from pygame.sprite import Sprite

class Ship(Sprite): 
    def __init__(self, polly):
        super().__init__()
        self.screen = polly.screen
        self.screen_rect = polly.screen.get_rect()
        self.settings = polly.settings 
        
        self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.scale(self.image, (140, 140))
        self.rect = self.image.get_rect()
        
        self.rect.midleft = self.screen_rect.midleft
        
        self.y = float(self.rect.y)
        
        self.moving_up = False
        self.moving_down = False
        
    def update(self):
        if self.moving_up and self.rect.top > 0: 
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        self.rect.y = self.y
        
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        
    def centre_ship(self):
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)
        
        
            
        