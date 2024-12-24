# 02/06/2022
import matplotlib.pyplot as plt

x_values = range(1, 6)
y_values = [x**3 for x in x_values]

ig, ax = plt.subplots()
ax.scatter(x_values, y_values, )

ax.axis([0, 6, 0, 130])

plt.show()

x_values2 = range(1, 5001)
y_values2 = [x**3 for x in x_values2]

ig, ax = plt.subplots()
ax.scatter(x_values2, y_values2, s=1)

plt.show()