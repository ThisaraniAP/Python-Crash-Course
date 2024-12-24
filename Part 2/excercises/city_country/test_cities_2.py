# 10/07/2021
import unittest
from city_functions import city_country_population

class LocationTestCase(unittest.TestCase):
	"""Tests for 'city_functions.py'."""

	def test_city_country(self):
		"""Do locations like 'Santiago, Chile' work?"""
		formatted_location = city_country_population('Santiago', 'Chile')
		self.assertEqual(formatted_location, 'Santiago, Chile')

	def test_city_country_population(self):
		"""Do locations and populations like 'Santiago, Chile - population 5000000' work?"""
		formatted_location = city_country_population('Santiago', 'Chile', 5000000)
		self.assertEqual(formatted_location, 'Santiago, Chile - population 5000000')

if __name__ == '__main__':
	unittest.main()