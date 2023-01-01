""" 

Developer : Melih Orhan Yilmaz
Date      : 28.12.2022

Application : The Least Common Multiple

Explanation : 
    As a user, I want to use a program which can calculate the least common multiple (L.C.M.) of four numbers. So that I can find the least 
    common multiple (L.C.M.) of my inputs.

    Acceptance Criteria:
    Ask user to enter the four numbers. Use try/except blocks to verify input entries and warn the user for Nan or non numerical inputs. 
    Calculate the least common multiple (L.C.M.) of four numbers Use gcd function in module of math (use import gcd function in math)

"""

from math import lcm

def lcm_abcd():
    while True:
        try:
            a=int(input("Enter 1st number: "))
            b=int(input("Enter 2nd number: "))
            c=int(input("Enter 3th number: "))
            d=int(input("Enter 4th number: "))
            lcm_numbers = lcm(a,b,c,d)
            break

        except ValueError:
            print('You have entered an invalid value.')

    return lcm_numbers

print("The result is", lcm_abcd())