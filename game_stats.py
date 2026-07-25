"""
Alien (cat) Invasion - Track 1
Daniel Shiloh
Track score, lives, level
Starter code from https://github.com/RedBeard41/alien_Invasion_starter
July 25, 2026
"""

from pathlib import Path
import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class GameStats:
    """track and store score, lives, level"""

    def __init__(self, game):
        """start at 0 points"""
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.init_saved_scores()
        self.reset_stats()

    def init_saved_scores(self):
        """read high score from file"""
        self.path = self.settings.scores_file
        if self.path.exists() and self.path.stat.__sizeof__() > 0:
            contents = self.path.read_text()
            scores = json.loads(contents)
            self.hi_score = scores.get('hi_score', 0)
        else:
            self.hi_score = 0  
            self.save_scores()          

    def save_scores(self):
        """write high score to file"""
        scores = {
            'hi_score': self.hi_score
        }
        contents = json.dumps(scores, indent=4)
        try:
            self.path.write_text(contents)
        except FileNotFoundError as e:
            print(f'File not found: {e}')

    def reset_stats(self):
        """game over"""
        self.ships_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1

    def update(self, collisions):
        """update all scores as needed"""
        self._update_score(collisions)
        self._update_max_score()
        self._update_hi_score()

    def _update_max_score(self):
        """update max score (current game)"""
        if self.score > self.max_score:
            self.max_score = self.score

    def _update_hi_score(self):
        """update hi score (of all games)"""
        if self.score > self.hi_score:
            self.hi_score = self.score

    def _update_score(self, collisions):
        """update current score, for current round of current game"""
        for alien in collisions.values():
            self.score += self.settings.alien_points

    def update_level(self):
        """increase level"""
        self.level += 1