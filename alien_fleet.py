"""
Alien (cat) Invasion - Track 1
Daniel Shiloh
Treat aliens as a group
Starter code from https://github.com/RedBeard41/alien_Invasion_starter
July 25, 2026
"""

import pygame
from alien import Alien
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class AlienFleet:

    def __init__(self, game: 'AlienInvasion'):
        """set up and create fleet"""
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed

        self.create_fleet()

    def create_fleet(self):
        """manage planning and placing of fleet"""
        alien_w = self.settings.alien_w
        alien_h = self.settings.alien_h
        screen_w = self.settings.screen_w
        screen_h = self.settings.screen_h

        fleet_w, fleet_h = self.calculate_fleet_size(alien_w, screen_w, alien_h, screen_h)

        x_offset, y_offset = self.calculate_offsets(alien_w, alien_h, screen_w, fleet_w, fleet_h)

        self._create_rectangle_fleet(alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset)

    def calculate_fleet_size(self, alien_w, screen_w, alien_h, screen_h):
        """from screen and alien sizes, find number of aliens to fit"""
        fleet_w = (screen_w//alien_w)
        fleet_h = ((screen_h / 2)//alien_h)

        if fleet_w % 2 == 0:
            fleet_w -= 1
        else:
            fleet_w -= 2

        if fleet_h % 2 == 0:
            fleet_h -= 1
        else:
            fleet_h -= 2

        return int(fleet_w), int(fleet_h)

    def calculate_offsets(self, alien_w, alien_h, screen_w, fleet_w, fleet_h):
        """from screen and alien sizes, find spacing at edges of screen"""
        half_screen = self.settings.screen_h//2
        fleet_horizontal_space = fleet_w * alien_w
        fleet_vertical_space = fleet_h * alien_h
        x_offset = int((screen_w - fleet_horizontal_space)//2)
        y_offset = int((half_screen - fleet_vertical_space)//2)
        return x_offset,y_offset
    
    def _create_rectangle_fleet(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset):
        """draw evenly-spaced aliens"""
        for row in range(fleet_h):
            for col in range(fleet_w):
                current_x = alien_w * col + x_offset
                current_y = alien_h * row + y_offset
                if col % 2 == 0 or row % 2 == 0:
                    continue
                self._create_alien(current_x, current_y)

    
    def _create_alien(self, current_x: int, current_y: int):
        """add alien to group of aliens"""
        new_alien = Alien(self, current_x, current_y)
        self.fleet.add(new_alien)

    def _check_fleet_edges(self):
        """once an alien hits an edge, drop the whole fleet"""
        alien: Alien
        for alien in self.fleet:
            if alien.check_edges():
                self._drop_alien_fleet()
                self.fleet_direction *= -1
                break

    def _drop_alien_fleet(self):
        """move aliens left, toward player"""
        for alien in self.fleet:
            alien.x -= self.fleet_drop_speed

    def update_fleet(self):
        """check if at wall, then find new pos"""
        self._check_fleet_edges()
        self.fleet.update()

    def draw(self):
        """draw each alien"""
        alien: 'Alien'
        for alien in self.fleet:
            alien.draw_alien()

    def check_collisions(self, other_group):
        """rm alien and bullet if collision"""
        return pygame.sprite.groupcollide(self.fleet, other_group, True, True)
    
    def check_fleet_left(self):
        """has hit left wall?"""
        alien: Alien
        for alien in self.fleet:
            if alien.rect.left <= 0:
                return True
        return False
    
    def check_destroyed_status(self):
        """is fleet empty?"""
        return not self.fleet