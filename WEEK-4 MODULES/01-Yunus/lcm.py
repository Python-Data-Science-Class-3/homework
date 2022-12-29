# The Least Common Multiple As a user, I want to use a program which
#  can calculate the least common multiple (L.C.M.) of four numbers. 
#  So that I can find the least common multiple (L.C.M.) of my inputs.

# Acceptance Criteria: Ask user to enter the four numbers. Use try/except 
# blocks to verify input entries and warn the user for Nan or non numerical inputs. 
# Calculate the least common multiple (L.C.M.) of four numbers Use gcd function in
#  module of math (use import gcd function in math


#-------------made by Yunus 26.12.2022---------------
from math import gcd
import sys

def prime_numbers(border):     #This function finds prime numbers between 0 and given value(border)
    c = []
    for i in range(2,border):
        for j in range(2,i):
            if i%j == 0 :
                break
        else:
            c.append(i)
    return c

def LCM_calculator(numbers):       #this function calculates LCM by using GCD
    global lcd1,lcd2,lcd

    #this formule works with 2 number therefore i had to do it twice-----------------------------------

    lcd1 = (numbers[0]*numbers[1])/gcd(numbers[0],numbers[1])   
    lcd2 = (numbers[2]*numbers[3])/gcd(numbers[2],numbers[3])

    lcd= (lcd1*lcd2)/gcd(int(lcd1),int(lcd2))
    print(f"the LCD of {numbers} is {lcd}")
    
while True:
    numbers = []
    try:
        numbers = list(map(int,input("Enter 4 number :").split()))  # takes 4 integers
        
    except :
        print("Oops, Error occured, please enter integers with a space in between")
    else :
        LCM_calculator(numbers)
        sys.exit()

    
            


