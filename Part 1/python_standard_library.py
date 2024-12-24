# 28/06/2021
"""
The Python standard library is a set of modules included with every python installation.
"""

from random import randint
print(randint(1, 6))
# randint() produces a random number between the given numbers

from random import choice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)
print(first_up)
# choice() returns a random value from a list or tuple

# You can also download modules from external sources