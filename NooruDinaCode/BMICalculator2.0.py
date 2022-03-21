"""
This program checks Body Mass Index (BMI) based on a user's weight and height
"""
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

'''
Instructions
Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese.
'''

print(color.DARKCYAN + '"Welcome! to BMI calculator 2.0"' + color.END)
"""
Data provided by the end users
"""
weight = float(input(color.BOLD +"Please provide the user weight : - \n"+ color.END))
height = float(input(color.BOLD +"Please provide the user height : - \n"+ color.END))

print("The BMI for the user is : - ")

BMI = weight/height**2
if BMI < 18.5:
    print(color.RED + "The user is underweight"+ color.END)
elif BMI > 18.5 and BMI < 25:
    print(color.GREEN + "The user is underweight"+ color.END)
elif BMI > 25 and BMI < 30:
    print(color.YELLOW + "The user is slightly overweight" + color.END)
elif BMI > 30 and BMI <= 35:
    print(color.RED + "The user is obese"+ color.END)
else:
    print(color.RED + "The user is clinically obese"+ color.END)
