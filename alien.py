"""
Alien (cat) Invasion - Track 1
Daniel Shiloh
Create aliens and their movement
Starter code from https://github.com/RedBeard41/alien_Invasion_starter
July 25, 2026
"""

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_fleet import AlienFleet

class Alien(Sprite):
    """create and move an alien within the boundaries"""
    
    def __init__(self, fleet: 'AlienFleet', x: float, y: float):
        """load alien at a location as part of a fleet"""

        super().__init__()
        self.fleet = fleet
        self.screen = fleet.game.screen
        self.boundaries = fleet.game.screen.get_rect()
        self.settings = fleet.game.settings

        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image,
            (self.settings.alien_w, self.settings.alien_h)
            )
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        """decide and set new position"""
        speed = self.settings.fleet_speed

        self.y += speed * self.fleet.fleet_direction
        self.rect.x = self.x
        self.rect.y = self.y

    def check_edges(self):
        """is touching top or bottom of screen?"""
        return ((self.rect.bottom >= self.boundaries.bottom) or (self.rect.top <= self.boundaries.top))
    
    def draw_alien(self):
        """draw to screen"""
        self.screen.blit(self.image, self.rect)