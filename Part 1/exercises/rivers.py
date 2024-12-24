# 23/05/2021
rivers = {
	'amazon' : 'brazil',
	'ganges' : 'india',
	'zhuang' : 'china',
	'nile' : 'egypt',
}

for river, country in rivers.items():
	print (f"The {river.title()} river runs through {country.title()}")

print ("\nRivers")
for river in rivers:
	print (river.title())

print ("\nCountries")
for country in rivers.values():
	print (country.title())