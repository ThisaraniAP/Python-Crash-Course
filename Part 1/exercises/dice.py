# 28/06/2021
from random import randint

class Die:
	"""A simple attempt to modle a die."""
	
	def __init__(self, sides=6):
		"""Initialize the number of sides."""
		self.sides = sides

	def roll_die(self):
		"""Simulate rolling the die."""
		print(randint(1, self.sides))


# Roll a 6-sided die 10 times
test_1 = Die()
test_1.roll_die()
test_1.roll_die()
test_1.roll_die()
test_1.roll_die()
test_1.roll_die()
test_1.roll_die()
test_1.roll_die()
test_1.roll_die()
test_1.roll_die()
test_1.roll_die()
print("\n")

# Roll a 10-sided die 10 times
test_2 = Die(sides=10)
test_2.roll_die()
test_2.roll_die()
test_2.roll_die()
test_2.roll_die()
test_2.roll_die()
test_2.roll_die()
test_2.roll_die()
test_2.roll_die()
test_2.roll_die()
test_2.roll_die()
print("\n")

# Roll a 20-sided die 10 times
test_3 = Die(sides=20)
test_3.roll_die()
test_3.roll_die()
test_3.roll_die()
test_3.roll_die()
test_3.roll_die()
test_3.roll_die()
test_3.roll_die()
test_3.roll_die()
test_3.roll_die()
test_3.roll_die()