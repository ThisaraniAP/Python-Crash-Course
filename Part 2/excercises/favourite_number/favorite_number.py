# 07/07/2021
import json

filename = 'favorite_number.json'

favorite_number = input("What is your favorite number? ")

with open(filename, 'w') as f:
    json.dump(favorite_number, f)
