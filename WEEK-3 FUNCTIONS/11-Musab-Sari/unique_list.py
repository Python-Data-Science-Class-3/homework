'''
Developer   : Musab SARI
Date        : 23.12.2022

Application : Unique List

Explanation : Unique list is an application where user enters items in a list and outputs unique items which do not repeat itself in that list.
'''

a = list(input('Please enter your list with a space between:').split(' '))

def unique_list(x):
    
    k = set()
    [k.add(x[i]) for i in range(len(x))]
    print(list(k))

unique_list(a)