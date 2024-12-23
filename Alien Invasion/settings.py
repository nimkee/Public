
class Settings:
    """A class to store all settings for Alien Invsasion"""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3

        # Bullet Settings

        self.bullet_width = 1100
        self.bullet_height = 15
        self.bullet_color = (80, 60, 60)
        self.bullets_allowed = 6

        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):
        """Initialize the settings that change throughout the game."""

        self.ship_speed = 10
        self.bullet_speed = 2.5
        self.alien_speed = 3.0

        # Score settings
        self.alien_points = 50
        # Fleet_direction of 1 represents right; -1 left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speeed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)







