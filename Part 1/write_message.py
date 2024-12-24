# 02/07/2021
filename = 'programming.txt'

# 'r' for read mode'w' for write mode, 'a' for append mode
with open(filename, 'w') as file_object:
	file_object.write("I love programming.\n")
	file_object.write("I love creating new games.\n")

# If a file with that name does not exist, Python will automatically create one.

with open(filename, 'a') as file_object:
	file_object.write("I also love finding meaning in large datasets.\n")
	file_object.write("I love creating apps that can run in a browser.\n")
# 'a' is used beacuse 'w' would erase the contents of the file if it already exists.