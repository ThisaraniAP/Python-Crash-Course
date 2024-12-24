# 05/07/2021
import json

filename = 'numbers.json'
with open(filename) as f:
	numbers  = json.load(f)

print(numbers)