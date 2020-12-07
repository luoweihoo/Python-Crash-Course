# @File    :   settings.py
# @Time    :   2020/11/14 16:09:24
# @Author  :   Wei Luo
# @Version :   1.0
# @Contact :   luoweihoo@yahoo.com
# @Desc    :   None

class Settings:
    """A class to store all settings for Alien Invasions."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5

