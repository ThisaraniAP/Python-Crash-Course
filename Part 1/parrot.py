# 02/06/2021
message = input("Tell me something, and I will repeat it back to you: ")
print (message)

# 04/06/2021
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end this part of the program. "
message = ""
while message != 'quit':
	message = input(prompt)
	if message != 'quit':
		print (message)

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
active = True
while active:
        message = input(prompt)
        if message == 'quit':
                active = False
        else:
                print(message)
