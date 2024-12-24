#14/07/2021
class Employee:
	"""Store information and give a raise to an employee."""

	def __init__(self, first_name, last_name, annual_salary):
		"""Store all of the attributes"""
		self.first_name = first_name
		self.last_name = last_name
		self.annual_salary = annual_salary

	def give_raise(self, increment_salary=5000):
		self.annual_salary += increment_salary