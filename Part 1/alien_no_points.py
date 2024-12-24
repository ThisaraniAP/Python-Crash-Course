# 20/05/2021
alien_0 = {'color' : 'green', 'speed' : 'slow'}

# The second argument is the default value.
point_value = alien_0.get('points', 'No point value assigned.')
print (point_value)

point_value = alien_0.get('points')
print (point_value)
print (alien_0)