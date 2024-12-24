# 14/05/2021
# Tuples are lists with elements that can't be changed and has () instead of []
dimensions = (200, 50)
print (dimensions[0])
print (dimensions[1])
# Tuple with only one element
my_t = (3,)
print (my_t)
for dimension in dimensions:
	print (dimension)
dimensions = (400, 100)
print ("\nModified dimensions:")
for dimension in dimensions:
	print (dimension)