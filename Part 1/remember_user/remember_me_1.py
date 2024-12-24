# 05/07/2021
import json

username = input("What is your name? ")

filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"we'll remember you when you come back, {username}!")
