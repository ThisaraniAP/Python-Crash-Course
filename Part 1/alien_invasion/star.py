# 10/08/2021 - 11/08/2021

import pygame
from pygame.sprite import Sprite

class Star(Sprite):
	"""A class to manage the stars in the background."""

	def __init__(self, ai_game):
		"""Initialize the alien  and set its starting position."""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings

		# Load the stars image and set its rect attribute.
		self.image = pygame.image.load('images/stars2.bmp')
		self.rect = self.image.get_rect()

		# Start each new star near the top left of the screen.
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Store the stars exact horizontal position.
		self.y = float(self.rect.y)

	def update(self):
		"""Move the stars down."""
		self.y -= self.settings.star_speed
		self.rect.y = self.y