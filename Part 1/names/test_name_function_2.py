# 10/07/2021
import unittest
from name_function import get_formatted_name_2

class NameTestCase(unittest.TestCase):
	"""Test for 'name_function.py'."""

	def test_first_last_name_2(self):
		"""Do names like 'Janis Jophlin' work."""
		formatted_name = get_formatted_name_2('janis', 'jophlin')
		self.assertEqual(formatted_name, 'Janis Jophlin')

	def test_first_last_middle_name_2(self):
		"""Do names like 'Wolfgang Amadeus Mozart' work?"""
		formatted_name = get_formatted_name_2(
			'wolfgang', 'mozart', 'amadeus')
		self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
	unittest.main()