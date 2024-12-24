#04/05/2021
# Square brackets ([]) indicate lists in Python and elements are divided by commas(,).
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print (bicycles)
# To access elements in a list, use the index number.Index positions start from 0.
print (bicycles[0])
print (bicycles[0].title())
# Asking for index -1 returns last element, -2 returns the second last element and so on.
print (bicycles[-1])
print (bicycles[-2])
print (bicycles[-3])
message = f"My first bicycle was a {bicycles[0].title()}."
print (message)