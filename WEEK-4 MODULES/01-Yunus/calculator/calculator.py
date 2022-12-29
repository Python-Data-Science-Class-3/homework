'''Mis Calculator As a user, I want to use a program which can calculate basic mathematical operations.
So that I can add, subtract, multiply or divide my inputs.

Acceptance Criteria: The calculator must support the Addition, Subtraction, Multiplication and 
Division operations. Define four functions in four files for each of them, with two float numbers
as parameters. To calculate the answer, use math.ceil() and get the next integer value greater 
than the result Create a menu using the print command with the respective options and take an input
choice from the user. Using if/elif statements for cases and call the appropriate functions. 
Use try/except blocks to verify input entries and warn the user for incorrect inputs. 
Ask user if calculate numbers again. To implement this, take the input from user Y or N.
(use import sys, ceil function in math)'''

#---------------Made by Yunus donmez  26.12.2022----------------
from math import ceil
import sys
from addition import addition             #Importing functions in 4 different file
from subtraction import subtraction
from division import division
from multiplication import multiplication

while True :                            #Enters while loop to keep asking for a new process
    try :
        x = float(input("x = "))
        y = float(input("y = ")) 
    except :
        print("Ooops ! Please enter a float or integer...")         #Raise an error if te inputs are not integer or float
        continue
    else :
        #Calculation menu
        choice = int(input('''what do you want to do please choose  
    1-Addition
    2-Substarction
    3-Multiplication
    4-Division\n'''))                           
        if choice == 1:
            addition(x,y)
        elif choice == 2:
            subtraction(x,y)
        elif choice == 3:
            multiplication(x,y)
        elif choice == 4:
            division(x,y)
    choice2 = input("Do you want to do another calculation (Y/N)\n")
    if choice2.lower() == "n":
        print("Fijne dag nog :)")
        sys.exit()                                              #exits current program
    else :
        None