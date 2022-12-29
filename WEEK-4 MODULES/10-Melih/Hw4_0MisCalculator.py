""" 

Developer : Melih Orhan Yilmaz
Date      : 29.12.2022

Application : Mis Calculator

Explanation : 
    As a user, I want to use a program which can calculate basic mathematical operations. So that I can add, subtract, multiply or divide my 
    inputs.

    Acceptance Criteria:
    The calculator must support the Addition, Subtraction, Multiplication and Division operations. Define four functions in four files for each 
    of them, with two float numbers as parameters. To calculate the answer, use math.ceil() and get the next integer value greater than the 
    result Create a menu using the print command with the respective options and take an input choice from the user. Using if/elif statements 
    for cases and call the appropriate functions. Use try/except blocks to verify input entries and warn the user for incorrect inputs. Ask 
    user if calculate numbers again. To implement this, take the input from user Y or N. (use import sys, ceil function in math)
"""

from Hw4_1Addition import add
from Hw4_2Subtraction import sub
from Hw4_3Multiplication import multiply
from Hw4_4Division import divide

while True:

    calculator_menu = int(input("\nWhat's your choice? \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n"))

    if calculator_menu == 1:
        while True:
            try:
                x = float(input("Please enter 1st float number: "))
                y = float(input("Please enter 2nd float number: "))
                print("The addition of the numbers:", add(x,y))
                break

            except ValueError:
                print("Oops, Error occured,Value Error")

    elif calculator_menu == 2:
        while True:
            try:
                x = float(input("Please enter 1st float number: "))
                y = float(input("Please enter 2nd float number: "))
                print("The subtraction of the numbers:", sub(x,y))
                break

            except ValueError:
                print("Oops, Error occured,Value Error")

    elif calculator_menu == 3:
        while True:
            try:
                x = float(input("Please enter 1st float number: "))
                y = float(input("Please enter 2nd float number: "))
                print("The multiplication of the numbers:", multiply(x,y))
                break

            except ValueError:
                print("Oops, Error occured,Value Error")

    else:
        while True:
            try:
                x = float(input("Please enter 1st float number: "))
                y = float(input("Please enter 2nd float number: "))
                print("The division of the numbers:", divide(x,y))
                break

            except ValueError:
                print("Oops, Error occured,Value Error")

            except ZeroDivisionError:
                print("Oops, Error occured,Zero Division Error")

    question = input("\nDo you want to calculate the numbers again? [Y/N] : ")
    if question == "n" or question == "N":
        break 
    else:
        pass