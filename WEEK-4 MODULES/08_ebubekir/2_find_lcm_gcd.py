"""
2 - The Least Common Multiple As a user,
I want to use a program which can calculate the least common multiple (L.C.M.) of four numbers.
So that I can find the least common multiple (L.C.M.) of my inputs.

"""
from math import gcd,lcm
try:
    n1=int(input("input 1. number:"))
    n2=int(input("input 2. number:"))
    n3=int(input("input 3. number:"))
    n4=int(input("input 4. number:"))
    ebob=gcd(n1,n2,n3,n4)
    ekok=lcm(n1,n2,n3,n4)

except ValueError:
    print("your entry must be integer !") 
except None:
    print("you must enry a number !") 

else:
    print("The gcd of theese numbers is=", ebob)
    print("The lcd of theese 4 numbers is=",ekok)
finally:
    print("finish")

