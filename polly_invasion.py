from random import random

from time import sleep

import sys 

import pygame

from ship import Ship

from bullet import Bullet

from settings import Settings 

from game_stats import GameStats

from scoreboard import Scoreboard

from button import Button

from alien import Alien 

class Polly: 
    def __init__(self):
        pygame.init()
        
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        
        pygame.display.set_caption("Pollyland Invasion")
        
        self.bg_color = (244, 194, 194)
        
        self.stats = GameStats(self)
        
        self.sb = Scoreboard(self)
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        self.game_active = False
        
        self.play_button = Button(self, "Start")
        
    def run_game(self):
        while True: 
            self._check_events()
            if self.game_active: 
                self._create_alien()
                self.ship.update()
                self.aliens.update()
                self._update_aliens()
                self._update_bullets()
            self._update_screen()
            self.clock.tick(60)
        
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                
    def _check_play_button(self, mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self.stats.reset_stats()
            self.sb.prep_score()
            self.sb.prep_ships()
            self.game_active = True
            
            self.bullets.empty()
            self.aliens.empty()
            
            self.ship.centre_ship()
            
            pygame.mouse.set_visible(False)
                
    def _keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullets()
                
    def _keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False 
            
    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
                if bullet.rect.right <= 0:
                    self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()
                    
    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, False, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        
        if not self.aliens:
            self.bullets.empty()
            self._update_aliens()
    
    def _update_aliens(self):
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
            
        self._check_aliens_left()
        
    def _ship_hit(self):
        if self.stats.ship_left > 0:
            self.stats.ship_left -= 1
            self.sb.prep_ships()
            self.bullets.empty()
            self.aliens.empty()
            self._create_alien()
            self.ship.centre_ship()
            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)
            
    def _check_aliens_left(self):
        for alien in self.aliens.sprites():
            if alien.rect.right <= 0:
                self._ship_hit()
                break
                          
    def _create_alien(self):
        if random() < self.settings.alien_frequency:
            alien = Alien(self)
            self.aliens.add(alien)   
    
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.ship.blitme()
        self.sb.show_score()
        
        if not self.game_active:
            self.play_button.draw_button()
       
        pygame.display.flip()
        
    def _fire_bullets(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
        
if __name__ == "__main__":
    polly = Polly()
    polly.run_game()
        