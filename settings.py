from pathlib import Path

class Settings:
    """settings for all game elements"""

    def __init__(self):
        """static settings"""
        self.name: str = "Alien (cat) Invasion - Track 1"
        self.screen_w = 800
        self.screen_h = 800
        self.fps = 30
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'
        self.difficulty_scale = 1.2
        self.scores_file = Path.cwd() / 'Assets' / 'file' / 'scores.json'

        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'cannon.png'
        self.ship_w = 66
        self.ship_h = 49

        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'mouse.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.impact_sound = Path.cwd() / 'Assets' / 'sound' / 'impactSound.mp3'

        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'cat.png'
        self.alien_w = 46
        self.alien_h = 49
        self.fleet_direction = 1

        self.button_w = 200
        self.button_h = 50
        self.button_color = (0,50,150)

        self.text_color = (255,255,255)
        self.button_font_size = 48
        self.HUD_font_size = 20
        self.font_file = Path.cwd() / 'Assets' / 'Fonts' / 'Silkscreen' / 'Silkscreen-Bold.ttf'

    def initialize_dynamic_settings(self):
        """dynamic / potentially-dynamic settings"""
        self.ship_speed = 8
        self.starting_ship_count = 3
        
        self.bullet_w = 27
        self.bullet_h = 46
        self.bullet_speed = 8
        self.bullet_amount = 8
        
        self.fleet_speed = 5
        self.fleet_drop_speed = 25

        self.alien_points = 1

    def increase_difficulty(self):
        """speed gameplay up"""
        self.ship_speed *= self.difficulty_scale
        self.bullet_speed *= self.difficulty_scale
        self.fleet_speed *= self.difficulty_scale