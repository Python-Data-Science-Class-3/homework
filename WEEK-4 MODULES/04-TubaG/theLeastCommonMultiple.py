'''Devoloper : Tuba GÜMÜS ESMEK
   Date      : 29.12.2022
   Subjeckt  : The Least Common 

'''
#As a user, I want to use a program which can calculate the least common multiple (L.C.M.) of four numbers.
#  So that I can find the least common multiple (L.C.M.) of my inputs.

#Acceptance Criteria:

#Ask user to enter the four numbers. 
# Use try/except blocks to verify input entries and warn the user for Nan or non numerical inputs. 
# Calculate the least common multiple (L.C.M.) of four numbers Use gcd function in module of math 
# (use import gcd function in math)


import math       #importing the math modüle
from math import gcd #importing  from math---> gcd
#checking correctness of values with try block
try:

   n1 = int(input("First number :"))
   n2 = int(input("Second number :"))
   n3 = int(input("third number:"))
   n4= int(input("fourth number:"))
except ValueError:       #if one of the numbers is not an integer value, it falls into the except block
    print("please, just a numeric value!")

#if the entered numbers are not incorrect, the code continues with else
else:

   ebob1 = math.gcd(n1,n2)   #first, find the greatest common divisor of the first two numbers with the Math.gcd module 
   ekok1 = ((n1*n2)/ebob1)   #second, when we multiply the first two numbers and divide by the number we found above.
                              #we find the L.C.M
   print("ekok1 :  {} ".format(ekok1))


  # THE FIRST AN SECOND STEPS ALSO APPLY TO THE OTHER TWO NUMBERS 
   ebob2 = math.gcd(n3,n4) 
   ekok2 = ((n3*n4)/ebob2)
   print("ekok2 :  {} ".format(ekok2))

   result_ekok = (ekok1* ekok2)/ (ebob1*ebob2)  
   # Multiply least commom divisor and divide by the greatest common divisor
   #Thus, find the L.C.M of 4 numbers
   print("result_ekok: {}".format(result_ekok))