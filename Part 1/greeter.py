# 02/06/2021
name = input("Please enter your name: ")
print (f"Hello, {name}!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print (f"Hello, {name}")

# 08/06/2021
print ("test")
def greet_user():
	print ("Hello!")
greet_user()

def greet_user(username):
	print (f"Hello, {username.title()}!")
greet_user('jesse')
# here, 'username' is a parameter and 'jesse' is an argument
# they are sometime called the opposite names

# 11/06/2021
def get_formatted_name(first_name, last_name):
	full_name = f"{first_name} {last_name}"
	return full_name.title()

while True:
	print ("\nPlease tell me your name:")
	print ("(enter 'q' at any time to quit)")
	
	f_name = input("First name: ")
	if f_name == 'q':
		break

	l_name = input("Last name: ")
	if l_name == 'q':
		break

	formatted_name = get_formatted_name(f_name, l_name)
	print (f"\nHello, {formatted_name}!")