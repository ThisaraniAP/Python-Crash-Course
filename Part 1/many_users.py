# 30/05/2021
users = {
	'aeinstien' : {
		'first' : 'albert',
		'last' : 'einstien',
		'location' : 'princeton',
		}, 
	'mcurie' : {
		'first' : 'marie', 
		'last' : 'curie', 
		'location' : 'paris', 
		}, 

	}

for username, user_info in users.items():
	print (f"\nUsername: {username}")
	full_name = f"{user_info['first']} {user_info['last']}"
	location = user_info['location']

	print (f"\tFull name: {full_name.title()}")
	print (f"\tLocation: {location.title()}")