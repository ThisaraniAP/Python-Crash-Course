# 13/06/2021
print ("I will add the numbers you enter and check if your answer is correct. ")
while True:
    numbers = input("\nHow many numbers are there? ")
    numbers = int(numbers)
    number = 0
    while numbers > 0:
        numbers -= 1
        number = number + int(input("What is the number? "))
    answer = int(input("What is the sum? "))
    if answer == number:
        print("You are smart!")
    else:
        print("You are stupid!")
    print (f"The answer was {number}!")
    retry = input("Do you want to do this again? (y/n)")
    if retry == 'n':
        break
