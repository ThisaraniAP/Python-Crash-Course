# 28/06/2021
from random import choice

possible_values = [5, 43, 27, 99, 46, 74, 8, 3, 56, 6, 'l', 'f', 'g', 'd', 'h']
winning_values = []

x = 1
while x < 5:
	x += 1
	winning_values.append(choice(possible_values))

print(f"Any ticket with the following values will win a prize:")
for value in winning_values:
	print(value)


my_ticket = []
number_of_loops = 0
while my_ticket != winning_values:
	number_of_loops += 1
	a = 1
	my_ticket = []
	while a < 5:
		a += 1
		my_ticket.append(choice(possible_values))

print(f"\nThe loop ran {number_of_loops} times before getting the correct values.")