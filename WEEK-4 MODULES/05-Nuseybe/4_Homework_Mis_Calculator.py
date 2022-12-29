# Mis Calculator
# As a user, I want to use a program which can calculate basic mathematical operations. 
# So that I can add, subtract, multiply or divide my inputs.
# Acceptance Criteria:
# The calculator must support the Addition, Subtraction, Multiplication and Division operations.
#  Define four functions in four files for each of them, with two float numbers as parameters. 
# To calculate the answer, use math.ceil() and get the next integer value greater than the result
#  Create a menu using the print command with the respective options and take an input choice from the user. 
# Using if/elif statements for cases and call the appropriate functions.
#  Use try/except blocks to verify input entries and warn the user for incorrect inputs.
#  Ask user if calculate numbers again. To implement this, take the input from user Y or N.
#  (use import sys, ceil function in math) 
# written by Nuseybe at 29.12.2022

import add_modul 
import sub_modul
import div_modul
import multi_modul
from math import *


print("Select operation.")                  # Select operation from menu
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")


try : 
    while True:
        choice = input("Enter choice(1/2/3/4): ")                   # take input from the user

        
        if choice in ('1', '2', '3', '4'):                          # check if choice is one of the four options
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                add1=add_modul.add(num1,num2)                       # import the addition function from modul 
                print(num1, "-", num2, "=", add1)

            elif choice == '2':
                sub1=sub_modul.sub(num1,num2)                        # import the substraction function from modul 
                print(num1, "-", num2, "=", sub1 )

            elif choice == '3':
                multi1=multi_modul.multi(num1,num2)                   # import the multiplication function from modul 
                print(num1, "*", num2, "=", multi1)

            elif choice == '4':
                div1=div_modul.div(num1,num2)                         # import the division function from modul 
                print(num1, "/", num2, "=", div1)
        
        
       
            next_calculation = input("Let's do next calculation? (yes/no): ")      # check if user wants another calculation
            if next_calculation == "no" or next_calculation == "n":                # break the while loop if answer is no
                break
    
except (ValueError, TypeError, ZeroDivisionError):
    print("Invalid Input")