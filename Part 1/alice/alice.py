# 03/07/2021
filename = 'alice.txt'

try:
	with open(filename, encoding='utf-8') as f:
		contents = f.read()
except FileNotFoundError:
	print(f"Sorry, the file {filename} does not exist.\n")
else:
# Try this part after moving the 'alice.txt' to the same file.
	words = contents.split()
	num_words = len(words)
	print(f"The file {filename} has about {num_words} words.")