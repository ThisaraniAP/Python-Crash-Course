# 01/06/2021
favourite_places = []
jhon = {
	'name' : 'jhon', 
	'favourite_places' : ['new york city', 'des plaines'], 
	}
favourite_places.append(jhon)

blyke = {
	'name' : 'blyke', 
	'favourite_places' : ['wilson', 'salisbury'], 
	}
favourite_places.append(blyke)

remi = {
	'name' : 'remi', 
	'favourite_places' : ['regina', 'new mills', 'salisbury'], 
	}
favourite_places.append(remi)

for name in favourite_places:
	print (f"\nName: {name['name'].title()}")
	print ("Favourite place(s):")
	for place in name['favourite_places']:
		print (f"\t{place.title()}")