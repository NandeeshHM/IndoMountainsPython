
#This module deals with all the operations realted to set manuplation
'''

farm_animals  = {'cow','sheep','hen','goat','horse'}
farm_animals.add('bull')
'''


#remove functionality
'''farm_animals.remove('cow')
print(farm_animals)

farm_animals.pop()
print(farm_animals)
'''

#adding data to a set

numbers = {*{}}

while len(numbers) <= 4:
    next_num = (input("Please enter single digit number which needs to be added"))
    numbers.add(next_num)
    print(numbers)
else:
    print("We crossed the prescribed lenght for the set")