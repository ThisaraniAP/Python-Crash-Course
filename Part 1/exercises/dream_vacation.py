# 07/06/2021
question = "What is your name? "
prompt = "If you could visit one place in the world, where would you go? "
repeat_question = "Would you like to let someone else answer?(yes/no) "
repeat = ""
poll = {}

while repeat != 'no':
        name = input(question)
        place = input(prompt)
        repeat = input(repeat_question)
        poll[name] = place

print ("\nDream Vacation Poll Results:")
for names, places in poll.items():
        print (f"{names}'s dream vaction location is {places}")
