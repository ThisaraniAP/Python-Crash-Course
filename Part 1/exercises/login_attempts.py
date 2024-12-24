# 19/06/2021
class User:
	""" Creat a user."""

	def __init__(self, first_name, last_name, username, location, age, login_attempts):
		"""Initialize fist and last name attributes."""
		self.first_name = first_name
		self.last_name = last_name
		self.username = username
		self.location = location
		self.age = age
		self.login_attempts = login_attempts

	def describe_user(self):
		"""Summarize the user's information."""
		print(f"{self.first_name} {self.last_name} is the name of user '{self.username}'.")
		print(f"{self.username} is {self.age} years old.")
		print(f"{self.username} is from {self.location}.")

	def greet_user(self):
		"""Print a personalized message to the user."""
		print(f"Hello, {self.username}!\n")

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

mori = User('Mori', 'Jin', 'Monkey King', 'Korea', 17, 5)

mori.describe_user()
mori.greet_user()

print(mori.login_attempts)
mori.increment_login_attempts()
mori.increment_login_attempts()
mori.increment_login_attempts()
print(mori.login_attempts)
mori.reset_login_attempts()
print(mori.login_attempts)