# 07/06/2021
repeat = ""

while repeat != 'no':    
    letter_1 = input("\nWhat is the first letter?(a/b/c) ")
    letter_2 = input("What is the second letter?(a/b/c) ")
    if letter_1.lower() == 'a':
       output = '3421'
    elif letter_1.lower() == 'b':
       output = '7865'
    elif letter_1.lower() == 'c':
       output = '1537'
    else:
       output = "Error. Please enter valid value."

    if letter_2.lower() == 'a':
       output += '3241'
    elif letter_2.lower() == 'b':
       output += '7654'
    elif letter_2.lower() == 'c':
       output += '8492'

    print (output)
    repeat = input("Do you want to do it again?(yes/no) ")
