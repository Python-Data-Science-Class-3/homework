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

#We receive user requests
print("Press 1 to addition number")
print("Press 2 to subtraction number")
print("Press 3 to multiplication number")
print("Press 4 to divison number")
  
#Choose option
      
try:
    while True: 
        choice = int(input("Press the number of the action you want to do(1-4)"))
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))    
           
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

        if new_transaction == "N":
            print("See you in other programs \U0001f44b")
            sys.exit()

except Exception :
    print("Entering a number between 1 and 4 is not that difficult. Please enter a valid NUMBER.!! \U0001f44a")
