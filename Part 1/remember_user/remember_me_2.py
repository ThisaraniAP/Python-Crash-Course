# 06/07/2021
import json
filename = 'username.json'

def greet_user():
    """Greet the user by name."""
    try:
        with open(filename) as f:
            username = json.load(f)

    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"we'll remember you when you come back, {username}!")

    else:
        print(f"Welcome back, {username}!")

greet_user()