"""
Author: Adem DOĞAN

Subject of the Program :Random Password As a user, I want to use a program which can
generate random password and display the result on user interface. So that I can generate
my password for any application.

Date :12/2022"""

import sys
import math

#Write functions for 4 math operations
def add (num1,num2):
    return num1+num2

def sub (num1,num2):
    return num1-num2

def mult (num1,num2):
    return num1*num2

def div (num1,num2):
    return num1/num2


while True: 
#We receive user requests
    print("Press 1 to addition number")
    print("Press 2 to subtraction number")
    print("Press 3 to multiplication number")
    print("Press 4 to divison number")
    print("Press 5 to exit")

#Choose option
    choice = int(input("Press the number of the action you want to do(1-5)"))
    
    if choice == '5':
        sys.exit()

    else:
#Check if the entered value is true or false.
        try:
         num1 = float(input("Enter first number: "))
         num2 = float(input("Enter second number: "))

        except ValueError:
            print("Invalid input. Please enter a valid number. \U0001f44a")
            continue
# Call the function        
    if choice == 1:
        print(math.ceil(add(num1,num2)))

    elif choice == 2:
        print(math.ceil(sub(num1,num2)))

    elif choice == 3:
        print(math.ceil(mult(num1,num2)))

    elif choice == 4 :
        print(math.ceil(div(num1,num2)))

    else:
        print("Invalid number")

    new_transaction =input("Do you want to calculate more numbers? (Y/N) ").upper()  

    if new_transaction == "Y":
        continue
    else:
        print("See you in other programs \U0001f44b")
        sys.exit()

### For the first input, we can avoid the error with try-except when an incorrect value is entered.
### Let's fix it, then resend.