current_users = ['phoebe', 'maya', 'Tanya', 'aarushi', 'Admin']
new_users = ['yuta', 'Phoebe', 'Mori', 'maya', 'Arlo']
for username in new_users:
	if username.lower() in current_users:
		print (f"the username '{username}' has already been used, please enter a new username.")
	else:
		print (f"The username '{username}' is available.")