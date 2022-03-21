#Program to calculate tip amoung group

#Banner for program
print("Welcome to the tip calculator \n")

#Entry for total bill
total_bill = float(input("Please enter the total bill amount : "))

#What percentage of tip you would like to give ?
tip_to_be_given = int(input("What percentage of tip would you like to give ? 10, 12 or 15 ? : "))

#Number of people in group
people_involved = int(input("How many people are pitching in for the bill ? : "))

#Final amount to be paid
each_person = (tip_to_be_given/100 * total_bill)
print(f"So each person has to pay {each_person} amount")