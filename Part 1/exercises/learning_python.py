# 01/07/2021
file_name = 'learning_python.txt'

with open(file_name) as file_object:
	contents = file_object.read()
print(contents)
print("\n\n")


with open(file_name) as file_object:
	contents = file_object.readlines()
for line in contents:
	print(line.rstrip())
print("\n\n")


text = ''
with open(file_name) as file_object:
	contents = file_object.readlines()
for line in contents:
	text += line
print(text)