import pygame

class Ship():

    def __init__(self, screen):
        """Initialize the ship and set its starting position."""

        self.screen = screen

        #Load the ship image and get ist rect
        self.image = pygame.image.load('images/ship2.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #START EACH NEW SHIP AT THE BOTTOM CENTER OF THE SCREEN
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom


    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)