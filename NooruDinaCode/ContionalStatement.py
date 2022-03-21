#Program to check the contional workflow


print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? \n "))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("But before we proceed, please provide your age ? \n "))
    if age <= 12:
        print("Please pay 5$ .")
    elif age > 12 and age < 18:
        print("Please pay 7$.")
    else:
        print("Please pay 12$")
else:
    print("Sorry, you have to grow taller before you can ride.")


'''
"""
THIS BLOCK HOLDS CODE FOR IF CONDITION STATEMENT
"""

#Program to check if a number is ODD or EVEN

print("Welcome to fact checking website")
userNumber = int(input("Please enter the number for which checking has to be applied "))
'''

'''

"""
ODD or EVEN Condition :
A number is said to be even numbers can be divided by 2 with no remainders
"""

if userNumber % 2 == 0:
    print("The given number is an even number")
else:
    print("The given number is an odd number")
    
'''