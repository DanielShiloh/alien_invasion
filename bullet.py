"""
Alien (cat) Invasion - Track 1
Daniel Shiloh
Create bullets to fire
Starter code from https://github.com/RedBeard41/alien_Invasion_starter
July 25, 2026
"""

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Bullet(Sprite):
    """Create bullet to be fired from ship"""
    
    def __init__(self, game: 'AlienInvasion'):
        """load bullet, start at right edge of ship"""

        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(self.image,
            (self.settings.bullet_w, self.settings.bullet_h)
            )
        
        self.rect = self.image.get_rect()
        self.rect.midright = game.ship.rect.midright
        self.x = float(self.rect.x)

    def update(self):
        """move bullet right"""
        self.x += self.settings.bullet_speed
        self.rect.x = self.x
    
    def draw_bullet(self):
        """draw bullet to screen"""
        self.screen.blit(self.image, self.rect)