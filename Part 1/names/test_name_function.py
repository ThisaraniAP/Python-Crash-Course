# 08/07/2021
import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
	"""Test for 'name_function.py'."""

	def test_first_last_name(self):
		"""Do names like 'Janis Jophlin' work."""
		formatted_name = get_formatted_name('janis', 'jophlin')
		self.assertEqual(formatted_name, 'Janis Jophlin')

if __name__ == '__main__':
	unittest.main()