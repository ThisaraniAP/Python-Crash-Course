motorcycles = ['honda', 'yamaha', 'suzuki']
print (motorcycles)

# Modifying elements in a list
motorcycles[0] = 'ducati'
print (motorcycles)

# Adding elements to the end of a list
print ("\n", motorcycles)
motorcycles.append('honda')
print (motorcycles)

# Lists can be built using '.append()'
motorcycle_types = []
motorcycle_types.append('honda')
motorcycle_types.append('yamaha')
motorcycle_types.append('suzuki')
print ("\n", motorcycle_types)

# Inserting elements into list
print ("\n", motorcycle_types)
motorcycle_types.insert(0, 'ducanti')
print (motorcycle_types)

# Removing elements from a list 1(del)
print ("\n", motorcycle_types)
del motorcycle_types[0]
print (motorcycle_types)
print ("\n", motorcycles)
del motorcycles[3]
print (motorcycles)

# Removing elements from a list 2(pop())
print ("\n", motorcycles)
popped_motorcycles = motorcycles.pop()
print (motorcycles)
print (popped_motorcycles)
print ("\n", motorcycles)
last_owned = motorcycles.pop()
print (f"\nThe last motorcycle I owned was a {last_owned.title()}.")
first_owned = motorcycles.pop(0)
print (f"\nThe first motorcycle I owned was a {first_owned.title()}.")

# Removing elements from a list 3(remove())
print ("\n", motorcycle_types)
motorcycle_types.remove('suzuki')
print (motorcycle_types)
too_expencive = 'yamaha'
motorcycle_types.remove(too_expencive)
print (motorcycle_types)
print (f"\nA {too_expencive.title()} is too expencive for me.")