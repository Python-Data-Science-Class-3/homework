"""
As a user, I want to use a program which can calculate
 the least common multiple (L.C.M.) of four numbers. 
 So that I can find the least common multiple (L.C.M.) of my inputs.

Acceptance Criteria:

Ask user to enter the four numbers. 
Use try/except blocks to verify input entries and warn
the user for Nan or non numerical inputs. 
Calculate the least common multiple (L.C.M.) of four numbers
 Use gcd function in module of math (use import gcd function in math)
"""
import math
import os 

n= []
def myLCM():
    while True:

        try:
            
            for i in range(1,5):
                
                num =int(input(" Enter a nummer for the least common multiple   :"))
                n.append(num)
                
                
                if (isinstance(n[(i-1)], int)):
                    print(f"{i}.th nummer is  {n[(i-1)]} ")
            
            mylcb= math.gcd(n[0],n[1],n[2],n[3])
            os.system("cls")
            print(f" The Least Common Multiple is {mylcb}\n")
            break

        except ValueError:
            print("The expression you entered must be a number(int) !")
            myLCM()
        
print("\n")
print("\nThe least common multiple (L.C.M.) of four numbers... ")
myLCM()