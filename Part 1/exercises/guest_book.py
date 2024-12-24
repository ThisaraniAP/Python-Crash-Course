# 02/07/2021
filename = 'guest_book.txt'

repeat = 'y'
while repeat == 'y':
	guest_name = input("\nWhat is your name? ")
	print(f"Welcome {guest_name.title()}!\n")
	with open(filename, 'a') as file_object:
		file_object.write(f"{guest_name}\n")
	repeat = input("Would you like to input another name?(y/n) ")
	while repeat != 'y' and repeat != 'n':
		print("\nInvalid value. Please enter 'y' or 'n'.")
		repeat = input("Would you like to input another name?(y/n) ")