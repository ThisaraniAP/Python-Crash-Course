# 10/07/2021
import unittest
from city_functions import city_country

class LocationTestCase(unittest.TestCase):
	"""Tests for 'city_functions.py'."""
	def test_city_country(self):
		"""Do locations like 'Santiago, Chile' work?"""
		formatted_location = city_country('Santiago', 'Chile')
		self.assertEqual(formatted_location, 'Santiago, Chile')

if __name__ == '__main__':
	unittest.main()