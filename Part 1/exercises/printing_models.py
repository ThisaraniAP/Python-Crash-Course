# 13/06/2021
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_designs:
	current_design = unprinted_designs.pop()
	print (f"Printing model: {current_design}")
	completed_models.append(current_design)

print ("\nThe following models have been printed: ")
for completed_model in completed_models:
	print (completed_model)
print ("\n")


# Reorganizing the code using functions:
def print_models(unprinted_designs, completed_models):
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print (f"Printing model: {current_design}")
		completed_models.append(current_design)

def show_completed_models(completed_models):
	print ("\nThe following models have been printed: ")
	for completed_model in completed_models:
		print (completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
print ("\n")


# Preventing a function from modifying a list
# For this, you can give the function a copy instead:
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:], completed_models)
print ("\n\n")

# 15/06/2021
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

from printing_functions import *

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)