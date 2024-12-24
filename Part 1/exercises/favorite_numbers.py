# 20/05/2021
favorite_numbers = {
	'Noah' : '9',
	'Jhon' : '15',
	'Mori' : '4',
	'Medea' : '14',
	'Scarlet' : '6'
	}
print (favorite_numbers, "\n")

# 01/06/2021
favorite_numbers = {
	'noah' : [9, 8], 
	'jhon' : [15, 62], 
	'mori' : 32,
	'medea' : [14, 68], 
	'scarlet' : 6, 
	}
for name in favorite_numbers.keys():
	print (f"\nName: {name.title()}")
	print (f"Favorite number(s): {favorite_numbers[name]}")