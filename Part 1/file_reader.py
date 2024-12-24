# 29/06/2021
with open('pi_digits.txt') as file_object:
	contents = file_object.read()
print(contents)
print("\n")

"""
If the .txt file isn't in the same file you can use

a relative file path:
with open('text_files/filename.txt') as file_object:

or an absolute file path(absolute paths are usually longer, so you can use variable):
file_path = '/home/ehmatthes/other/files/text_files/text_files/filename.txt'
with open(file_path) as file_object:
"""

filename = 'pi_digits.txt'

with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())
print("\n")

with open(filename) as file_object:
	lines = file_object.readlines()
pi_string = ''
for line in lines:
	pi_string += line.rstrip()
print(pi_string)
print(len(pi_string))
print("\n")

with open(filename) as file_object:
	lines = file_object.readlines()
pi_string = ''
for line in lines:
	pi_string += line.strip()
print(pi_string)
print(len(pi_string))
print("\n")

filename = 'pi_million_digits.txt'
with open(filename) as file_object:
	lines = file_object.readlines()
pi_string = ''
for line in lines:
	pi_string += line.rstrip()
print(f"{pi_string[:52]}...")
print(len(pi_string))

for line in lines:
	pi_string += line.rstrip()
birthday = input("Enter your birthday, in the form of ddmmyy: ")
if birthday in pi_string:
	print("Your birthday appears in the first million digits of pi!")
else:
	print("Your birthday does not appear in the first million digits of pi.")
