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

import sys           #importing sys and math
import math

from math import ceil 

from add import addition              #math operations(+,-,*,/) imported from four other files
from substract import substraction
from multiply import multiplication
from divide import division

#starting processes with While True loop
while True:  
    operations= int(input("1-addition\n2-substraction\n3-multiplication\n4-division\n, choice :"))
    
    try:
        a= float(input("enter  first number:"))
        b= float(input("enter second number:"))
       
        
    except ValueError:    #the except blok displays the error if the value is not a numeric value

      print("Oops, Error occured, Value Error")
      continue

    #processing with the if loop
    #round the number up by one with ceil function
    if operations == 1 :
         print("addition : {}". format(math.ceil(addition(a,b))))
        

           
    elif   operations == 2:
        print("substraction: {}".format(math.ceil(substraction(a,b))))


    elif operations == 3:
        print("multiplication : {}".format(math.ceil(multiplication(a,b))))

    #with the try except block, an error is indicated if the second number is "0"
    try:
        if operations == 4 and b==0:
            print("division : {}".format(math.ceil(division(a,b))))
         

    except ZeroDivisionError:
        print("sifira bölüm olmaz")
  
    operation2= (input("if you want to you countinue: Y/N "))  
    if operation2 == "Y":
        continue
     #exiting the program
    else:
        print("exit")
        sys.exit()   

