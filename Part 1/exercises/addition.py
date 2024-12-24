# 13/06/2021
print ("Give me two numbers and I'll add them.")
while True:
    number_1 = input("\nFirst number: ")
    try:
        number_1 = int(number_1)
    except ValueError:
        print("Please enter a number\n")
    else:
        number_2 = input("Second number: ")
        try:
            number_2 = int(number_2)
        except ValueError:
            print("Please enter a number\n")
        else:
            answer = number_1 + number_2
            print (f"The sum is {answer}!")
            retry = input("\nDo you want to add again? (y/n)")
            while retry != 'y' and retry != 'n':
                print("\nPlease enter 'y' or 'n'.")
                retry = input("Do you want to add again? (y/n)")
            if retry == 'n':
                break
