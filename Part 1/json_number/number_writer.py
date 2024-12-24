# 05/07/2021
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f:
	json.dump(numbers, f)

# This should automatically creat the 'numbers.json' file in the same folder