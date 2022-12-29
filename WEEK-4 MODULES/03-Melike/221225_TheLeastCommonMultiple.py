"""
2 - The Least Common Multiple 
As a user, I want to use a program which can calculate the least common multiple (L.C.M.) of four numbers. 
So that I can find the least common multiple (L.C.M.) of my inputs.

Acceptance Criteria: 
Ask user to enter the four numbers. 
Use try/except blocks to verify input entries and warn the user for Nan or non numerical inputs. 
Calculate the least common multiple (L.C.M.) of four numbers 
Use gcd function in module of math (use import gcd function in math)"""

from math import lcm

while True:
    try:
        a = int(input("\nFirst: "))
        b = int(input("Second: "))
        c = int(input("Third: "))
        d = int(input("Fourth: "))
        lcm_abcd = lcm(a,b,c,d)
        print(f"The least common multiple of those four number is {lcm_abcd}.")
        break

    except ValueError:
        print("Error occured.. Please enter a number..")
