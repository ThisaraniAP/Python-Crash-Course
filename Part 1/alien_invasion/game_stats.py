# 10/08/2021 - 27/08/2021

class GameStats:
	"""Track statistics."""

	def __init__(self, ai_game):
		"""Initialize statistics."""
		self.settings = ai_game.settings
		self.reset_stats()

		# Start alien invation in an inactive state.
		self.game_active = False
		self.game_lost = False

		# High Score should never be reset.
		self.high_score = 0

	def reset_stats(self):
		"""Initialize settings that can change during the game."""
		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.level = 1