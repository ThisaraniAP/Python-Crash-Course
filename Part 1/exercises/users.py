# 16/06/2021
class User:
	""" Creat a user."""

	def __init__(self, first_name, last_name, username, location, age):
		"""Initialize fist and last name attributes."""
		self.first_name = first_name
		self.last_name = last_name
		self.username = username
		self.location = location
		self.age = age

	def describe_user(self):
		"""Summarize the user's information."""
		print(f"{self.first_name} {self.last_name} is the name of user '{self.username}'.")
		print(f"{self.username} is {self.age} years old.")
		print(f"{self.username} is from {self.location}.")

	def greet_user(self):
		"""Print a personalized message to the user."""
		print(f"Hello, {self.username}!\n")

mori = User('Mori', 'Jin', 'Monkey King', 'Korea', 17)
daewi = User('Daewi', 'Han', "Sage's eye", 'Korea', 34)
mira = User('Mira', 'Yoo', 'The Arm of the Sage', 'Korea', 34)

mori.describe_user()
mori.greet_user()

daewi.describe_user()
daewi.greet_user()

mira.describe_user()
mira.greet_user