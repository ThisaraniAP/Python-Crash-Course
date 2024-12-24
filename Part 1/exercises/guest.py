# 02/07/2021
filename = 'guest.txt'
guest_name = input("Please enter your name. ")

with open(filename, 'w') as file_object:
	file_object.write(guest_name)