# 15/06/2021
import pizzas
pizzas.making_pizza(16, 'pepperoni')
pizzas.making_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

from pizza import making_pizza_1
making_pizza_1(16, 'pepperoni')
making_pizza_1(12, 'mushrooms', 'green peppers', 'extra cheese')

from pizza import making_pizza_1 as mp1
mp1(16, 'pepperoni')
mp1(12, 'mushrooms', 'green peppers', 'extra cheese')

import pizzas as p
p.making_pizza(16, 'pepperoni')
p.making_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

from pizzas import *
making_pizza(16, 'pepperoni')
making_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')