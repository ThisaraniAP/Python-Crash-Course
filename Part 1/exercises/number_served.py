# 18/06/2021
class Restaurant:
	"""Informs about a restaurant"""
	
	def __init__(self, restaurant_name, cuisine_type, number_served=0):
		"""Initialize name and cuisine type attributes."""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = number_served

	def describe_restaurant(self):
		"""Describe the restaurant."""
		print(f"The restaurant's name is {self.restaurant_name}.")
		print(f"It has a {self.cuisine_type} cuisine.")

	def open_restaurant(self):
		"""Indicate that the restaurant is open"""
		print(f"{self.restaurant_name} is now open!")

	def set_number_served(self, customers):
		self.number_served = customers

	def increment_number_served(self, consumers):
		self.number_served += consumers


restaurant = Restaurant('Devon', 'Indian')
restaurant.describe_restaurant()
restaurant.open_restaurant()
print("\n")

print(restaurant.number_served)
restaurant = Restaurant('Devon', 'Indian', number_served=10)
print(restaurant.number_served)
print("\n")

restaurant = Restaurant('Devon', 'Indian')
print(restaurant.number_served)
restaurant.set_number_served(15)
print(restaurant.number_served)
print("\n")

restaurant = Restaurant('Devon', 'Indian')
print(restaurant.number_served)
restaurant.set_number_served(22)
print(restaurant.number_served)
restaurant.increment_number_served(5)
print(restaurant.number_served)
print("\n")
