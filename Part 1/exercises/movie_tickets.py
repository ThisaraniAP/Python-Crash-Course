# 05/06/2021
prompt = "Enter me your age and I will tell you how much a ticket will cost:"
prompt += "\nEnter 'quit' to exit the program."
active = True
while active:
    age = input(prompt)
    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            cost = "free"
        elif age < 12:
            cost = "$10"
        else:
            cost = "$15"
        print (f"Your movie ticket is {cost}.")
