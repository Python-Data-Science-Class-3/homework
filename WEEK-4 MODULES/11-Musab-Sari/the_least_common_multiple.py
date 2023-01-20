'''
Developer   : Musab SARI
Date        : 01.01.2023

Application : The Least Common Multiple

Explanation : The Least Common Multiple is an application where user can find the least common multiple of user-inputted 4 numbers.
'''
    
from math import gcd

def least_common_multiple(x):
    return print(gcd(x[0],x[1],x[2],x[3]))

user_input = input("Enter your numbers with a coma(,) in between them:").split(',')
while True:

    for entries in user_input:
        
        try:
            
            entries = int(entries)      
        
        except ValueError:
            
            print ('NaN/ Non numerical value')

            break    

    least_common_multiple(list(map(int, user_input)))