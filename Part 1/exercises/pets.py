# 01/06/2021
pets = []
timmy = {
	'name' : 'timmy', 
	'gender' : 'male', 
	'type' : 'dog', 
	'breed' : 'labrador', 
	'owner_name' : 'phoebe hegeler', 
	}
pets.append(timmy)

smudge = {
	'name' : 'smudge', 
	'gender' : 'female', 
	'type' : 'cat', 
	'breed' : 'japanese bobtail', 
	'owner_name' : 'maya joshi', 
	}
pets.append(smudge)

lola = {
	'name' : 'lola', 
	'gender' : 'female', 
	'type' : 'bird', 
	'breed' : 'parrot', 
	'owner_name' : 'tanvi dalmia', 
	}
pets.append(lola)

print ("Pets\n")
for pet in pets:
	print (f"Name:\t{pet['name'].title()}")
	print (f"Gender:\t{pet['gender'].title()}")
	print (f"Type:\t{pet['type'].title()}")
	print (f"Breed:\t{pet['breed'].title()}")
	print (f"Owner's name:\t{pet['owner_name'].title()}\n")