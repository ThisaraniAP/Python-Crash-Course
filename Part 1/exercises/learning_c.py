# 01/07/2021
file_name = 'learning_python.txt'

with open(file_name) as file_object:
	contents = file_object.read()
contents = contents.replace('Python', 'C')
print(contents)