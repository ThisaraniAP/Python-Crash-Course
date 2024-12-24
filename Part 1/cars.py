# 11/05/2021
# Organizing lists
# sort() arranges the list in alphabetically order permanently
cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort()
print (cars)
# sort(reverse=True) arranges the list in reverse alphabetically order
cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort(reverse=True)
print ("\n", cars)
# sorted() arranges the list in alphabetically order temporarily and also accepts a reverse=True
cars = ["bmw", "audi", "toyota", "subaru"]
print ("\n\nHere is the original list :")
print (cars)
print ("\nHere is the sorted list :")
print (sorted(cars))
print ("\nHere is the original list again :")
print (cars)
print ("\nHere is the reverse sorted list :")
print (sorted(cars, reverse=True))
print ("\nHere is the original list again :")
print (cars)
# reverse() arrages the list in reverse order permenently and also accepts a reverse=True
cars = ["bmw", "audi", "toyota", "subaru"]
print ("\n\n", cars)
cars.reverse()
print (cars)
# you can revert the original order by using reverse() again
cars.reverse()
print (cars)
# len() finds the length of a list
print ("\n\n", cars)
print (len(cars))

# 15/05/2021
# if statement
cars = ['audi', 'bmw', 'subaru', 'toyota']
print ("\n\n")
for car in cars:
	if car == 'bmw':
		print (car.upper())
	else:
		print (car.title())

#checking for equality
car = 'bmw'
print ("\n", car == 'bmw')
car = 'audi'
print (car == 'bmw')
car = 'Bmw'
print (car == 'bmw')
car = 'Bmw'
print (car.lower() == 'bmw')
print (car)