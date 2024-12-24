# 07/06/2021
sandwich_orders = ['cheese sandwich', 'vegetable sandwich', 'meat sandwich', 'egg sandwich']
finished_sandwiches = []
while sandwich_orders:
	sandwich = sandwich_orders.pop()
	print (f"Your {sandwich} has been made!")
	finished_sandwiches.append(sandwich)
print ("\nSandwichs that were made:")
for finished_sandwiche in finished_sandwiches:
	print (f"\t{finished_sandwiche.title()}")