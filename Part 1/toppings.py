# 15/05/2021
requested_topping = ("mushrooms")
if requested_topping != "anchovies":
	print ("Hold the anchovies!")
requested_topping = ("anchovies")
if requested_topping != "anchovies":
	print ("Hold the anchovies!")
else:
	print ("Anchovies topping!")

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print ('mushrooms' in requested_toppings)
print ('pepperoni' in requested_toppings, "\n\n")

# testing multiple conditions
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
	print ("Adding mushrooms")
if 'pepperoni' in requested_toppings:
	print ("Adding pepperoni")
if 'extra cheese' in requested_toppings:
	print ("Adding extra cheese")
print ("\nFinished making your pizza!\n\n")
# elif would not work here
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
	print ("Adding mushrooms")
elif 'pepperoni' in requested_toppings:
	print ("Adding pepperoni")
elif 'extra cheese' in requested_toppings:
	print ("Adding extra cheese")
print ("\nFinished making your pizza!\n\n")

# 16/05/2021
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
	print (f"Adding {requested_topping}.")
print ("Finished making your pizza!\n")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print ("Sorry, we are out of green peppers right now.")
	else:
		print (f"Adding {requested_topping}.")
print ("Finished making your pizza!\n")

# When a list name is used in if statements, Python return False if the list is empty
requested_toppings = []
if requested_toppings:
	for requested_topping in requested_toppings:
		print (f"Adding {requested_topping}.")
	print ("Finished making your pizza!\n")
else:
	print ("Are you sure you want a plain pizza?\n\n")

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print (f"Adding {requested_topping}.")
	else:
		print (f"Sorry, we don't have {requested_topping}.")
print ("Finished making your pizza!\n")