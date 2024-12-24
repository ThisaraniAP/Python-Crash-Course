# 05/07/2021
import json

filename = 'username.json'

with open(filename) as f:
	username = json.load(f)
	print(f"Welcome back, {username}")