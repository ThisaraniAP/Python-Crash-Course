# 02/07/2021
filename = 'programming_poll.txt'

repeat = 'y'
while repeat == 'y':
	reason = input("\nWhy do you like programming? ")
	with open(filename, 'a') as file_object:
		file_object.write(f"{reason}\n")
	repeat = input("Would you like to input another reason?(y/n) ")
	while repeat != 'y' and repeat != 'n':
		print("\nInvalid value. Please enter 'y' or 'n'.")
		repeat = input("Would you like to input another name?(y/n) ")