# 21/08/2021 - 27/08/2021
import pygame

class GameOver:
	"""Display the 'Game over!' when all the lives are lost"""

	def __init__(self, ai_game):
		"""Initialize the 'Game over!' and set its starting position."""
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		# Load the 'Game over!' image and get its rect.
		self.image = pygame.image.load('images/Game over!.bmp')
		self.rect = self.image.get_rect()

		# Display the 'Game over!' centre of the screen.
		self.rect.center = self.screen_rect.center

		"""Display the 'Game over!'."""
		self.screen.blit(self.image, self.rect)