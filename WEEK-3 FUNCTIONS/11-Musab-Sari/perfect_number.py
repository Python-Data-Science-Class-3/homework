'''
Developer   : Musab SARI
Date        : 23.12.2022

Application : Perfect Number

Explanation : Perfect number is an application where you can enter a range where your perfect numbers are to be searched. Perfect number is meaning that
a number which equals to sum of its divisors except the number itself.
'''
from functools import reduce

a = int(input('In what range would you like your perfect number to be searched:'))
k = []

def perfect_number(x):
    t = []
    [t.append(y) for y in range(1,a) if x%y == 0 and x != y]
    
    if sum(t) == x:
        
        k.append(x) 
        return

for i in range(6,a+1):
    perfect_number(i)

print('\nPerfect numbers in the range you setted are:', k)

new_list = filter(lambda x: x<1000, k)
print('\nThe sum of perfect numbers in the range of 1000 is:', reduce(lambda x,y:x+y, new_list))
print('\nIf your range is lower than 1000 then you will see the sum up to your range!')