'''
Developer   : Musab SARI
Date        : 01.01.2023

Application : Calculator

Explanation : Calculator is an application where user can do 4 basic mathematical operations(Addition, Subtraction, Multiplication, Division). 
'''

from math import ceil
import sys


def addition(a,b):
    
    return ceil(a + b)

def subtraction(a,b):
    
    return ceil(a - b)

def multiplication(a,b):
    
    return ceil(a * b)

def division(a,b):
    
    return ceil(a / b)

while True:
    
    try:
        
        user_input = int(input(('''\n1 = Addition
2 = Subtraction
3 = Multiplication
4 = Division
5 = Quit
Choose an option between 1-5:''')))
        
        if user_input == 1:
            
            num1_input = float(input('Number 1:'))
            num2_input = float(input('Number 2:'))
            
            print(f"\n{num1_input}+{num2_input}={addition(num1_input,num2_input)}")
        
        elif user_input == 2:
            
            num1_input = float(input('Number 1:'))
            num2_input = float(input('Number 2:'))
            
            print(f"\n{num1_input}-{num2_input}={subtraction(num1_input,num2_input)}")
        
        elif user_input == 3:
            
            num1_input = float(input('Number 1:'))
            num2_input = float(input('Number 2:'))
            
            print(f"\n{num1_input}*{num2_input}={multiplication(num1_input,num2_input)}")
        
        elif user_input == 4:
            
            num1_input = float(input('Number 1:'))
            num2_input = float(input('Number 2:'))
            
            print(f"\n{num1_input}/{num2_input}={division(num1_input,num2_input)}")
        
        elif user_input == 5:
            
            print("The calculator terminated its function!")
            
            sys.exit()
        
        else:
            
            print("Please enter a number between 1-5")
        
    except ZeroDivisionError:
        
        print("Number 1 cannot be divided to '0'!")
        
    except ValueError:
        
        print('Entered invalid value')