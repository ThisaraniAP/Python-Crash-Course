# 03/07/2021
# Python has objects called exceptions to manage errors.
# You can write code that handles exceptions.
# This means you can personalize the traceback and make it easier understand.


try:
	print(5/0)
except ZeroDivisionError:
	print("You can't divide by zero!\n")


print("Give me two numbers, and I'll divide them.")
print("Enter 'q' anytime to quit.")

while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break
	second_number = input("\nSecond number: ")
	if first_number == 'q':
		break
	try:
		answer = int(first_number) / int(second_number)
	except ZeroDivisionError:
		print("You can't divide by 0!")
	else:
		print(answer)