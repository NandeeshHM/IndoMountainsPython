#Program to get name added into GPU  wait list
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

customer_name = input('Enter Your Name \n')
interested_model = input('Enter the model which you want to buy \n')

print(color.RED + 'Dear {0}, model {1} has been added to our list and same will be notified once its available in the inventory'.format(customer_name, interested_model) + color.END)