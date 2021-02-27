# @File    :   ship.py
# @Time    :   2020/11/14 16:50:48
# @Author  :   Wei Luo
# @Version :   1.0
# @Contact :   luoweihoo@yahoo.com
# @Desc    :   None

import pygame

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal postion.
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.x = self.x
            
    def blitme(self):
        """Draw the ship at its current locations."""
        self.screen.blit(self.image, self.rect)
