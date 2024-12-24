# 13/06/2021
messages = ['Hello!', 'How are you?', "I'm good!", 'Thank you!']

def show_messages(messages):
	for message in messages:
		print (message)

show_messages(messages)
print ("\n")


sent_messages = []
def send_messages(messages, sent_messages):
	while messages:
		message = messages.pop()
		print (message)
		sent_messages.append(message)

send_messages(messages, sent_messages)

print ("\n")
print (messages)
print (sent_messages)