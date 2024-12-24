# 07/06/2021
sandwich_orders = ['cheese sandwich', 'pastrami sandwich', 'pastrami sandwich', 'vegetable sandwich', 
	'meat sandwich', 'pastrami sandwich', 'egg sandwich']
finished_sandwiches = []
print ("Sorry, we are out of pastrami!\n")
while 'pastrami sandwich' in sandwich_orders:
	sandwich_orders.remove('pastrami sandwich')
while sandwich_orders:
	sandwich = sandwich_orders.pop()
	print (f"Your {sandwich} has been made!")
	finished_sandwiches.append(sandwich)
print ("\nSandwichs that were made:")
for finished_sandwiche in finished_sandwiches:
	print (f"\t{finished_sandwiche.title()}")