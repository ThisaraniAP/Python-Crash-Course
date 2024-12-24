# 18/07/2021 - 11/08/2021
import sys
import pygame
from time import sleep

from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien
from star import Star

class AlienInvasion:
	"""Overall class to managegame assets and behaviour."""
	
	def __init__(self):
		"""Initialize the game and create game resources."""
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption("Alien Invasion")

		# Create an instance to store game statistics.
		self.stats = GameStats(self)

		self.stars = pygame.sprite.Group()
		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()

		self._create_star_fleet()
		self._create_fleet()

	def run_game(self):
		"""Start the main loop for the game."""
		while True:
			self._check_events()

			if self.stats.game_active:
				self.ship.update()
				self._update_bullets()
				self._update_aliens()
				self._update_stars()
			
			self._update_screen()

	def _check_events(self):
		""" Respond to keypresses and mouse events."""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

	def _check_keydown_events(self, event):
		"""Respond to keypresses."""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

	def _check_keyup_events(self, event):
		"""Respond to key releases."""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False

	def _fire_bullet(self):
		"""Create a new bullet and add it to the bullet group."""
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _update_bullets(self):
		"""Update position and bullets and get rid of old bullets."""
		# Update bullet positions.
		self.bullets.update()

		# Get rid of the bullets that have dissapeared.
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)

		# Check for any bullets that have hit aliens.
		# If so then get rid of the alien and the bullet.
		self._check_bullet_alien_collisions()

	def _check_bullet_alien_collisions(self):
		"""Respond to bullet-alien collisions."""
		# Remove any bullets and aliens that have collided.
		collisions = pygame.sprite.groupcollide(
		self.bullets, self.aliens, True, True)

		if not self.aliens:
			# Destroy existing bullets and create new fleet.
			self.bullets.empty()
			self._create_fleet()

	def _update_aliens(self):
		"""
		Check if the is at an edge,
		  then update the position of all the aliens in the fleet.
		"""
		self._check_fleet_edges()
		self.aliens.update()

		# Look for alien-ship collitions.
		if pygame.sprite.spritecollideany(self.ship, self.aliens):
			self._ship_hit()

		# Look for aliens hitting the bottom of the screen.
		self._check_aliens_bottom()
	
	def _create_fleet(self):
		"""Create the fleet of aliens."""
		# Create an alien and find the number of aliens in a row.
		# Spacing between each alien is equal to one alien width.
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		available_space_x = self.settings.screen_width - (2 * alien_width)
		number_aliens_x = available_space_x // (2 * alien_width)

		# Determine the number of rows of aliens that fits on the screen.
		ship_height = self.ship.rect.height
		available_space_y = (self.settings.screen_height - 
								(3 * alien_height) - ship_height)
		number_rows = available_space_y // (2 * alien_height)

		# Create a full fleet of aliens.
		for row_number in range(number_rows):
			for alien_number in range(number_aliens_x):
				self._create_alien(alien_number, row_number)

	def _create_alien(self, alien_number, row_number):
		"""Create an alien and place it in the row."""
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x = alien.x
		alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
		self.aliens.add(alien)

	def _check_fleet_edges(self):
		"""Respond appropriately if any aliens have reached the edge."""
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
				break

	def _change_fleet_direction(self):
		"""Drop the entire fleet and change the fleet's direction."""
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.fleet_drop_speed
		self.settings.fleet_direction *= -1
		
	def _update_screen(self):
		"""Update images on the screen, and flip to the new screen."""
		self.screen.fill(self.settings.bg_color)
		self.stars.draw(self.screen)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.aliens.draw(self.screen)

		pygame.display.flip()

	def _ship_hit(self):
		"""Respond to the ship being hit by an alien."""
		if self.stats.ships_left > 0:
			# Decrement the ships_left.
			self.stats.ships_left -= 1

			# Get rid of any remaining aliens and bullets.
			self.aliens.empty()
			self.bullets.empty()

			# Create a new fleet and centre the ship.
			self._create_fleet()
			self.ship.centre_ship()

			# Pause.
			sleep(0.5)
		else:
			self.stats.game_active = False

	def _check_aliens_bottom(self):
		"""Check if any aliens have reached the bottom of the screen."""
		screen_rect = self.screen.get_rect()
		for alien in self.aliens:
			if alien.rect.bottom >= screen_rect.bottom:
				# Treat this the same as if the ship got hit.
				self._ship_hit()
				break

	def _update_stars(self):
		"""Update position of stars and get rid of old star."""
		# Update stars positions.
		self.stars.update()
		
		# Get rid of the stars that have dissapeared.
		for star in self.stars.copy():
			if star.rect.bottom <= 0:
				self.stars.remove(star)
				for star_number in range(self.number_stars_x):
					self._create_star(star_number, self.number_rows)

	def _create_star_fleet(self):
		"""Create an star and place it in the row."""
		# Create an star and find the number of stars in a row.
		star = Star(self)
		star_width, star_height = star.rect.size
		available_space_x = self.settings.screen_width - (0)
		self.number_stars_x = available_space_x // (star_width)

		# Determine the number of rows of stars that fits on the screen.
		ship_height = self.ship.rect.height
		available_space_y = (self.settings.screen_height)
		self.number_rows = available_space_y // (star_height)

		# Create a full fleet of stars.
		for row_number in range(self.number_rows+1):
			for star_number in range(self.number_stars_x):
				self._create_star(star_number, row_number)

	def _create_star(self, star_number, row_number):
		"""Create an star and place it in the row."""
		star = Star(self)
		star_width, star_height = star.rect.size
		star.x = star_width * star_number
		star.rect.x = star.x
		star.y = star.rect.height * row_number
		self.stars.add(star)



if __name__ == '__main__':
	# Make a game instance, and run the game.
	ai = AlienInvasion()
	ai.run_game()