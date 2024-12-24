# 13/05/2021
# Slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print (players, "\n")
print (players[0:3])
print (players[1:4])
print (players[:4])
print (players[2:])
print (players[-3:])
print (players[:-3])
print (players[:])
print (players[0:4:2])
print ("\nHere are the first three players on my team:")
for player in players[:3]:
	print (player.title())
