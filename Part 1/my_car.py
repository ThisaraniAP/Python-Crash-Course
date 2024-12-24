# 22/06/2021
from car_2 import Car

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
print("\n")


from car_2 import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
print("\n")


import car_2

my_beetle = car_2.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = car_2.ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
print("\n")


from car_2 import Car
from electric_car_2 import ElectricCar

my_beetle = Car('volkswagen', 'beetle', '2019')
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
print("\n")
