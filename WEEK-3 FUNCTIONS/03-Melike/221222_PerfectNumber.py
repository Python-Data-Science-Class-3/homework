"""
4-perfect_number.py
Perfect number: Perfect number is a positive integer that is equal to the sum of its proper divisors.
The smallest perfect number is 6, which is the sum of 1, 2, and 3.
Some other perfect numbers are 28(1+2+4+7+14=28), 496 and 8128.

Write a function that finds perfect numbers between 1 and 1000. 
Check perfect numbers between 1 and 1000 and find the sum of the perfect numbers using reduce and filter functions.
"""

import functools

def perfect_number(num):
    sum_num = 0
    for i in range(1, num):
        if num%i == 0:                     # to find proper divisors of the number
            sum_num += i                   # to sum the proper divisors
    if sum_num == num:
        return True
    else:
        return False

def perfect_list(a, b):
    list1 = list(filter (perfect_number, range(a, b+1))) # to make a list with perfect_number function
    sum_list = functools.reduce(lambda x, y: x+y, list1) # to sum the elements of the list
    return sum_list

print(perfect_list(1,1000))

'''
Gayet guzel.

Bir de 
return sum_num == num
seklinde kurudugumuzda, bize True ya da False dondurecektir. If-Else dongusu kurmamiza gerek kalmadan da yapabiliriz.
'''
