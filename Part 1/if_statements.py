# 15/05/2021
# simple if statements
age =  19
if age >= 18:
	print ("You are old elnough to vote!")
	print ("Have you registered to vote yet?\n")

# if else statements
age =  17
if age >= 18:
	print ("You are old elnough to vote!")
	print ("Have you registered to vote yet?\n")
else:
	print ("You are too young to vote.")
	print ("Please register to vote as soon as you turn 18!\n")

# if elif else
age = 12
if age < 4:
	print ("your admission cost is $0.\n")
elif age < 18:
	print ("Your admission cost is $25.\n")
else:
	print ("Your admission cost is $40.\n")

age = 44
if age < 4:
	price = 0
elif age < 18:
	price = 25
else:
	price = 40
print (f"Your admission cost is ${price}.\n")


# multiple elif blocks
age = 70
if age < 4:
	price = 0
elif age < 18:
	price = 25
elif age < 65:
	price = 40
else:
	price = 20
print (f"Your admission cost is ${price}.\n")

# omitting else block
age = 56
if age < 4:
	price = 0
elif age < 18:
	price = 25
elif age < 65:
	price = 40
elif age >= 65:
	price = 20
print (f"Your admission cost is ${price}.\n")