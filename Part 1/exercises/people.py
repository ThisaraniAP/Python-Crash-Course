# 20/05/2021
person = {
	'first_name' : 'phoebe',
	'last_name' : 'hegeler',
	'age' : 14,
	'country' : 'india',
	}
print (person, "\n\n")


# 30/05/2021
phoebe = person
maya = {
	'first_name' : 'maya',
	'last_name' : 'joshi',
	'age' : 14,
	'country' : 'india',
	}
tanvi = {
	'first_name' : 'tanvi',
	'last_name' : 'dalmia',
	'age' : 15,
	'country' : 'india',
	}
people = [phoebe, tanvi, maya]

for person in people:
	name = f"{person['first_name']} {person['last_name']}"
	print (f"{name.title()} is {person['age']} years old"
		f" and lives in {person['country'].title()}.")

print ("\n")
for person in people:
	name = f"{person['first_name']} {person['last_name']}"
	print (f"\nName: {name.title()}")
	print (f"Age: {person['age']}")
	print (f"Country: {person['country'].title()}")