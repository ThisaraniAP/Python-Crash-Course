# 13/05/2021
pizzas = ['cheese pizza', 'corn pizza', 'pepperoni pizza']
for pizza in pizzas:
	print (f"I like {pizza}.")
print ("\nI really love pizza!")

friends_pizzas = pizzas[:]
pizzas.append('vegetable pizza')
friends_pizzas.append('mushroom pizza')
print ("\nMy favourite pizzas are:")
for pizza in pizzas:
	print (pizza)
print ("\nMy friend's favourite pizzas are:")
for pizza in friends_pizzas:
	print (pizza)