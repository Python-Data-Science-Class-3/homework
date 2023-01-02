"""
As a user, I want to use a program which can calculate basic mathematical operations.
 So that I can add, subtract, multiply or divide my inputs.

Acceptance Criteria:

The calculator must support the Addition, Subtraction, 
Multiplication and Division operations. Define four functions in four files for each of them, 
with two float numbers as parameters. To calculate the answer, use math.ceil() 
and get the next integer value greater than the result Create a menu using 
the print command with the respective options and take an input choice from the user. 
Using if/elif statements for cases and call the appropriate functions. Use try/except blocks to verify
 input entries and warn the user for incorrect inputs. Ask user if calculate numbers again. To implement this, 
 take the input from user Y or N.
  (use import sys, ceil function in math)
"""
import sys
import os
import math
from Add import *
from subtraction import *
from multiplication import *
from division import *
# from Areyousure import *


def Areyousure():
    
    while True:
        offer= input("Don't you want to do the calculate again ? Y(es) or N(o) ")
        
        if offer.upper()== "Y" :  
            os.system('cls')
            print("Select operation.")
            menu()
        if offer.upper()== "N": 
            sys.exit()    # or break you can  use




def menu():

    while True:
        calculatorMenu = int(input("\n1. Sum \
                                     \n 2.subtraction\
                                     \n 3.division\
                                     \n 4.multiplication\
                                     \n5. Exit \
                                     \n choes (1 - 5 )\n "))
        
        if calculatorMenu == 5 :
          print(" Exit process ")
          sys.exit()  

        
        try:
            num1= float(input("enter first nummer : "))
            #Is the value we get with the input a float? is not it? we check.
            if (isinstance(num1, float)):   
                num2= float(input("enter second nummer : "))

                if (isinstance(num2, float)):
                    
                    if calculatorMenu == 1 :
                        print(" collection process ")
                        add(num1,num2)
                    elif calculatorMenu == 2 :
                        print(" subtraction process ")
                        subt(num1,num2)
                    elif calculatorMenu == 3 :
                        print(" division process ")
                        divis(num1,num2)
                    elif calculatorMenu == 4 :
                        print(" multiplication process ")
                        multiplication(num1,num2)
                    if calculatorMenu == 5 :
                        print(" Exit process ")
                        break

                    

        except ValueError:
            print("Non float value...") 
        Areyousure()        



print("Select operation.\n")

menu()
