# 21/06/2021
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



class Admin(User):
	"""Creat a administrator."""

	def __init__(self, 
		first_name, 
		last_name, 
		username, 
		location, 
		age, 
		login_attempts, privileges=['can add post', 'can delete post', 'can ban user']):
		
		"""Initialize the admin's attributes."""
		super().__init__(first_name, last_name, username, location, age, login_attempts)
		self.privileges = privileges

	def show_privileges(self):
		"""Display the admin's privileges."""
		print("\nAdministrators have the following privileges:")
		for privilege in self.privileges:
			print(f"- {privilege}")

mori = Admin('Mori', 'Jin', 'Monkey King', 'Korea', 17, 5)

mori.show_privileges()
mori.describe_user()