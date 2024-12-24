# 04/07/2021
filenames = ['cats.txt', 'dogs.txt']

# Try this without moving both files to the same folder as this
for file in filenames:
	try:
		with open(file) as file_object:
			contents = file_object.read()
	except FileNotFoundError:
		print(f"The {file} file wasn't found.\n")
	else:
		print(f"{contents}\n")