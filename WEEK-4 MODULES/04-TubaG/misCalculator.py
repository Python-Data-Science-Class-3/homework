'''Devoloper : Tuba GÜMÜS ESMEK
   Date      : 29.12.2022
   Subjeckt  : Mis Calculator

'''
# Mis Calculator

#As a user, I want to use a program which can calculate basic mathematical operations. So that I can add, subtract, multiply or divide my inputs.

#Acceptance Criteria:

#The calculator must support the Addition, Subtraction, Multiplication and Division operations. 
# Define four functions in four files for each of them, with two float numbers as parameters. 
# To calculate the answer, use math.ceil() and get the next integer value greater than the result Create a menu using the print command with the respective options and
# take an input choice from the user. Using if/elif statements for cases and call the appropriate functions. 
# Use try/except blocks to verify input entries and warn the user for incorrect inputs. Ask user if calculate numbers again.
#To implement this, take the input from user Y or N. (use import sys, ceil function in math)

import sys
import math
from math import *
from math import ceil
def addition(a,b):
    return a+b
    

def substraction(a,b):
    return(a-b)


def multiplication(a,b):
    return(a*b)

def division(a,b):
    return(a/b)   


operations= input("1-addition\n2-substraction\n3-multiplication\n4-division\n, choice :")
try:
 
     a= float(input("enter  first number:"))
     b= float(input("enter second number:"))
     if operations == 1 :
            print("addition: {}".format(addition(a+b))) 
    

except TypeError: 

    print("Oops, Error occured, Value Error")


except ZeroDivisionError:
    print("Oops, Error occured, Zero Divion Error")




    
    a= float(input("enter  first number:"))
    b= float(input("enter second number:"))
     
    if operations == 2:
        print("substraction: {}".format(substraction(a-b)))


    if operations == 3:
        print("multiplication : {}".format(multiplication(a*b)))

    elif operations == 4:
        print("division : {}".format(division(a/b)))  

      
new_operations = input("new operations: Y/N")
reply = input("Y/N")
if reply == "N":
   break