#Program to find a string is palindrome or not


string = "malayalam"

reverse_string= (string[::-1])

if string == reverse_string:
    print("The string entered is palindrome")
else:
    print("Entered string is not a palidrome")


def mypalidrom(orgstring,revstring):
    revstring = orgstring[::-1]
    if revstring == orgstring:
        print("The entered string is an palidrome")
    else:
        print("The string is not an palindrome")

output = mypalidrom('malayalam',revstring)



