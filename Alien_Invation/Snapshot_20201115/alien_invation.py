# @File    :   alien_invation.py
# @Time    :   2020/11/14 11:57:23
# @Author  :   Wei Luo
# @Version :   1.0
# @Contact :   luoweihoo@yahoo.com
# @Desc    :   None

import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvation:
    """Overall class to manage game assests and behavior."""

    def __init__(self):
        """Intialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and return the game.
    ai = AlienInvation()
    ai.run_game()
