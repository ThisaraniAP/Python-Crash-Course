# 14/06/2021
def make_sandwich(*fillings):
	print ("\nMaking a sandwich with:")
	for filling in fillings:
		print (f"- {filling}")

make_sandwich('cheese')
make_sandwich('egg', 'tomatoes', 'lettuce')
make_sandwich('peanut butter', 'jam')