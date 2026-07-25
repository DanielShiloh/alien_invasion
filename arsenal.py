"""
Alien (cat) Invasion - Track 1
Daniel Shiloh
Treat bullets as a group
Starter code from https://github.com/RedBeard41/alien_Invasion_starter
July 25, 2026
"""

import pygame
from typing import TYPE_CHECKING
from bullet import Bullet

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    

class Arsenal:
    """Create group to manage list of bullets"""

    def __init__(self, game: 'AlienInvasion'):
        """create bullets as a group"""
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self):
        """update list of bullet to track"""
        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self):
        """remove bullets from right of screen"""
        for bullet in self.arsenal.copy():
            if bullet.rect.left >= self.settings.screen_w:
                self.arsenal.remove(bullet)

    def draw(self):
        """draw each bullet"""
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self):
        """is bullet available?  add if so"""
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False