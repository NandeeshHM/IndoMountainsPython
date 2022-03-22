"""
Python Program for Pizza Order
Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25

Pepperoni for small Pizza:$2
Pepperoni for Medium Or Large Pizza:$3

Extra cheese for any size pizza: $1;
"""

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L : ")
#add_pepperoni = input("Do you want pepperoni? Y or N :")
#extra_cheese = input("Do you want extra cheese? Y or N : ")

pizza_price = 0

Total_Bill = 0

#Pizza Order Details
if size == 'S':
    pizza_price += 15
    print(f'The size of the pizza selected is {size}, hence {pizza_price} is added to your active bill')
elif size == 'M':
    pizza_price += 20
    print(f'The size of the pizza selected is {size}, hence {pizza_price} is added to your active bill')
else:
    pizza_price += 25
    print(f'The size of the pizza selected is L, hence 25 is added to your active bill')

#Module for Pepperoni
add_pepperoni = input("Do you want pepperoni? Y or N :")
if add_pepperoni == 'Y':
    if size == 'S':
        pizza_price += 2
    else:
        pizza_price += 3
else:
    print("Pepperoni has not beeen selected. Hence it wont be added")


#Module for #extra_cheese = input("Do you want extra cheese? Y or N\n : ")
extra_cheese = input("Do you want extra cheese? Y or N : ")
if extra_cheese == 'Y':
    pizza_price += 1
else:
    print("Extra cheese is not added")

#Total Bill of pizza

Total_Bill = pizza_price
print(f'So you have to pay {Total_Bill}')