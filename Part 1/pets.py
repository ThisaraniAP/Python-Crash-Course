# 06/06/2021
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print (pets)

while 'cat' in pets:
	pets.remove('cat')

print (pets, "\n")


# 08/06/2021
def describe_pet(animal_type, pet_name):
	print (f"\nI have a {animal_type}.")
	print (f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')

describe_pet('dog', 'willie')

# The positions matter
describe_pet('willie', 'dog')

# but they don't if you use keywork arguments
describe_pet(animal_type = 'dog', pet_name = 'willie')
describe_pet(pet_name = 'willie', animal_type = 'dog')

# You can also use default values
def describe_pet(pet_name, animal_type = 'hamster'):
	print (f"\nI have a {animal_type}.")
	print (f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name = 'harry')

# You can change the default values
describe_pet(pet_name = 'willie', animal_type = 'dog')


# Different ways to achieve same output
def describe_pet(pet_name, animal_type = 'dog'):
	print (f"\nI have a {animal_type}.")
	print (f"My {animal_type}'s name is {pet_name.title()}.")

# A dog named Willie
describe_pet('willie')
describe_pet(pet_name = 'willie')

# A hamster named Harry
describe_pet('harry', 'hamster')
describe_pet(pet_name = 'harry', animal_type = 'hamster')
describe_pet(animal_type = 'hamster', pet_name = 'harry')