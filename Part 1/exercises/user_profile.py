# 14/06/2021
def build_profile(first, last, **user_info):
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

user_profile = build_profile('albert', 'einstein', 
							location = 'princeton', 
							field = 'physics')
print (user_profile)

# This is an exercise
user_profile = build_profile('thisarani', 'pathiranage', 
							gender = 'female', 
							age = 14, 
							location = 'india')
print (user_profile)