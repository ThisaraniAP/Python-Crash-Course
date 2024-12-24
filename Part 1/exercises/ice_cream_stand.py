# 20/06/2021

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



class IceCreamStand(Restaurant):
	"""A simple attempt to model a ice-cream stand."""

	def __init__(self, restaurant_name, cuisine_type, flavors):
		"""Initializes the ice cream stand's attributes."""
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = flavors

	def show_flavors(self):
		"""Display the available ice cream flavors."""
		print("\nThe following flavors are available:")
		for flavor in self.flavors:
			print(f"- {flavor}")



my_stand = IceCreamStand('Ice Cream!', 
	'dessert', 
	['chocolate', 'vanilla', 'strawberry', 'mint and chocolate chip', 'bubblegum'])

my_stand.describe_restaurant()
my_stand.open_restaurant()
my_stand.show_flavors()