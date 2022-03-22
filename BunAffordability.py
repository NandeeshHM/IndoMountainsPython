#Program to Add two numbers

price_num = int(input('Enter the price of the product \n \t'))
tax_num = int(input('Enter the tax rate in your region \n \t'))

#Function to estimate the total cost of the product

total_cost = str(price_num + tax_num)
print('Total billable amount of the product is ' + total_cost)
print('The {0} of the product with {1} is {2}'.format(price_num,tax_num,total_cost))