# 28/06/2021
from random import choice

possible_values = [5, 43, 27, 99, 46, 74, 8, 3, 56, 6, 'l', 'f', 'g', 'd', 'h']
winning_values = []

x = 1
while x<5:
	x += 1
	winning_values.append(choice(possible_values))

print(f"Any ticket with the following values will win a prize:")
for value in winning_values:
	print(value)