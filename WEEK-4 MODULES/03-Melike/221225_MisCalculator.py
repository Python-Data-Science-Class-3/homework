"""
4- Mis Calculator 
As a user, I want to use a program which can calculate basic mathematical operations. 
So that I can add, subtract, multiply or divide my inputs.

Acceptance Criteria: 
The calculator must support the Addition, Subtraction, Multiplication and Division operations. 
Define four functions in four files for each of them, with two float numbers as parameters. 

To calculate the answer, use math.ceil() and get the next integer value greater than the result 
Create a menu using the print command with the respective options and take an input choice from the user. 
Using if/elif statements for cases and call the appropriate functions. 
Use try/except blocks to verify input entries and warn the user for incorrect inputs. 
Ask user if calculate numbers again. To implement this, take the input from user Y or N. (use import sys, ceil function in math)"""

from math import ceil
#import sys

def add(x,y):
    return ceil(x+y)
def subt(x,y):
    return ceil(x-y)
def mult(x,y):
    return ceil(x*y)
def div(x,y):
    return ceil(x/y)

while True:
    try: 
        opp = (input("\nA-->Addition\nS-->Subtraction\nM-->Multiplication\nD-->Division\nPlease write the letter to choose the mathematical operation: ")).upper()
        num1= float(input("Please input first number: "))
        num2= float(input("Please input second number: "))
        if opp == "A":
            print(f"RESULT: {add(num1,num2)}")
        elif opp == "S":
            print(f"RESULT: {subt(num1,num2)}")
        elif opp == "M":
            print(f"RESULT: {mult(num1,num2)}")
        elif opp == "D":
            print(f"RESULT: {div(num1,num2)}")
        else: 
            print("Please input a letter from the list..")
        
        final = (input("Do you want to calculate again? (Y-->Yes of N-->No): ")).upper()
        if final == "Y": 
            continue
        elif final == "N":
            break
    
    except ZeroDivisionError:
        print("Second number can not be zero in division operation..")
    
    except ValueError:
        print("Please input a number..")
