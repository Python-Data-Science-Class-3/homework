#2 - The Least Common Multiple
# As a user, I want to use a program which can calculate the least common multiple (L.C.M.) of four numbers. 
# So that I can find the least common multiple (L.C.M.) of my inputs.
# Acceptance Criteria:
# Ask user to enter the four numbers. Use try/except blocks to verify input entries and warn the user for Nan or non numerical inputs.
#  Calculate the least common multiple (L.C.M.) of four numbers Use gcd function in module of math (use import gcd function in math)
#written by Nuseybe at 29.12.2022

import sys
import math

num1, num2, num3, num4=[int(a) for a in input("Please write 4  numbers:  ").split()]   #user input numbers for calculating

try:
    print(f"GCD is {math.gcd(num1,num2,num3,num4)}")                        #using gcd function from math modul
    print (f"LCM is {(num1*num2*num3*num4)/math.gcd(num1,num2,num3,num4)}")    #using gcd function for calculating lcm
    
except (TypeError, ValueError):                                             #for error using except.
    print("Opps !! an Error. Please input new numbers")
