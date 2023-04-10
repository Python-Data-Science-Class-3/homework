"""
Author: Adem DOĞAN

Subject of the Program :The Least Common Multiple As a user, I want to use a program which can calculate
the least common multiple (L.C.M.) of four numbers. So that I can find the least common
multiple (L.C.M.) of my inputs.

FORMULA: lcm(a,b,c,d) =(a*b*c*d)/gcd(abc,abd,acd,bcd)

Date :12/2022
"""
from math import gcd

#We create a function that calculates lcm using the formula in the description.
def calculate_lcm(a, b, c, d):
    gcd_value = gcd((a*b*c), (a*b*d),(a*c*d),(b*c*d))
    lcm = (a * b * c * d) / gcd_value
    return lcm

# Ask the user to enter the four numbers
a = input("Enter the first number: ")
b = input("Enter the second number: ")
c = input("Enter the third number: ")
d = input("Enter the fourth number: ")

# Verify that the input is a valid number
# For control numbers
try:
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
except Exception:
    print("Check the entered value")

# We call the function we defined and calculate the lcm of the 4 numbers entered.
else:
    lcm = calculate_lcm(a, b, c, d)
    print("The LCM of the four numbers is:", lcm)


### Use try/except blocks to verify input entries and warn the user for Nan or non numerical inputs.
### When I try to make an input of the wrong type, it returns the following error and stops.

"""
Invalid input. Please enter a valid number.
Traceback (most recent call last):
...
TypeError: 'str' object cannot be interpreted as an integer
"""
