# 15/07/2021
import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
	"""Test for the class Employee."""

	def setUp(self):
		"""Store the attributes to be used in the tests."""
		self.my_employee = Employee('Khun', 'Agnes', 25000)

	def test_give_default_raise(self):
		"""Test that the default raise works properly."""
		self.my_employee.give_raise()
		self.assertEqual(self.my_employee.annual_salary, 30000)

	def test_give_custom_raise(self):
		"""Test that a custom raise works properly."""
		self.my_employee.give_raise(increment_salary=3000)
		self.assertEqual(self.my_employee.annual_salary, 28000)

if __name__ == '__main__':
	unittest.main()