"""
2 - The Least Common Multiple 
As a user, I want to use a program which can calculate the least common multiple (L.C.M.) of four numbers. 
So that I can find the least common multiple (L.C.M.) of my inputs.

Acceptance Criteria: 
Ask user to enter the four numbers. 
Use try/except blocks to verify input entries and warn the user for Nan or non numerical inputs. 
Calculate the least common multiple (L.C.M.) of four numbers 
Use gcd function in module of math (use import gcd function in math)"""

from math import gcd

def lcm_finder_4_num(*nums):
    lcm_first = int(nums[0]*nums[1]/gcd(nums[0], nums[1]))
    lcm_second = int(nums[2]*nums[3]/gcd(nums[2], nums[3]))

    lcm_final = lcm_first * lcm_second / gcd (lcm_first, lcm_second)
    return lcm_final

while True:
    try:
        a = int(input("\nFirst: "))
        b = int(input("Second: "))
        c = int(input("Third: "))
        d = int(input("Fourth: "))
        lcm_abcd = lcm_finder_4_num(a,b,c,d)
        print(f"\nThe least common multiple of those four number is {lcm_abcd}.")
        break

    except ValueError:
        print("Error occured.. Please enter a number..")

### Good done!
### But it's allowed to use gcd method, not lcm. Could you use gcd method in place of lcm? Create a self lcm funtion if you want, it's allowed.