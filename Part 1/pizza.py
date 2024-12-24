# 28/05/2021
# Store information about a pizza being ordered.
pizza = {
	'crust' : 'thick', 
	'toppings' : ['mushrooms', 'extra cheese'], 
}

# Summarize the order.
print (f"You ordered a {pizza['crust']}-crust pizza "
	"with the following toppings:")

for topping in pizza['toppings']:
	print ("\t" + topping + "\n")


# 14/06/2021
def making_pizza(*toppings):
	print (toppings)
making_pizza('pepperoni')
making_pizza('mushrooms', 'green peppers', 'extra cheese')
print ("\n")

def making_pizza(*toppings):
	print ("\n Making a pizza with the following toppings:")
	for topping in toppings:
		print (f"- {topping}")
making_pizza('pepperoni')
making_pizza('mushrooms', 'green peppers', 'extra cheese')
print ("\n")

def making_pizza_1(size, *toppings):
	print (f"\n Making a {size}-inch pizza with the following toppings:")
	for topping in toppings:
		print (f"- {topping}")
making_pizza_1(16, 'pepperoni')
making_pizza_1(12, 'mushrooms', 'green peppers', 'extra cheese')
print ("\n")