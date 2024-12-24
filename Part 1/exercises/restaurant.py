# 16/06/2021
class Restaurant:
	"""Informs about a restaurant"""
	
	def __init__(self, restaurant_name, cuisine_type):
		"""Initialize name and cuisine type attributes."""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		"""Describe the restaurant."""
		print(f"The restaurant's name is {self.restaurant_name}.")
		print(f"It has a {self.cuisine_type} cuisine.")

	def open_restaurant(self):
		"""Indicate that the restaurant is open"""
		print(f"{self.restaurant_name} is now open!")

restaurant = Restaurant('Devon', 'Indian')
restaurant.describe_restaurant()
restaurant.open_restaurant()