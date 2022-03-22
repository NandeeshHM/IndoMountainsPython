

#Program to execute n integer

n = int(input('Enter the value of n \n\t'))

if n <= 100:
    if (n % 2) == 0:
        if 2 >= n <= 5:
            print('Not Weird')
        elif 6 >= n <= 20:
                print('Weird')
        else:
                print('Not Weird')
    else:
        print('Weird')
else:
    print('Please enter value of n less then 100')
