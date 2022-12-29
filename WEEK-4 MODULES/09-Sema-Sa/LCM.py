import math
from math import gcd
x=first_number=int(input("Please enter the first number:"))
y=second_number=int(input("Please enter the second number:"))
z=third_number=int(input("Please enter the third number:"))
t=fourth_number=int(input("Please enter the fourth number: "))


gcd_numbers=math.gcd(x,y,z,t)
lcm_numbers= (x*y*z*t)/gcd_numbers

print ("GCD = ",gcd_numbers)
print ("LCM = ",lcm_numbers)