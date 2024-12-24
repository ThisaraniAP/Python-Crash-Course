# 05/06/2021
prompt = "Please enter what topping you would like on your pizza:"
prompt += "\nEnter 'quit' to exit the program."
pizza_topping = ""

while pizza_topping != 'quit':
	pizza_topping = input(prompt)
	if pizza_topping == 'quit':
		break
	else:
		print (f"I will add {pizza_topping} to your pizza.")