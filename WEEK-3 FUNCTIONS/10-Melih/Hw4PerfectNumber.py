""" 

Developer : Melih Orhan Yilmaz
Date      : 22.12.2022

Application : Perfect Number

Explanation : 
    Perfect number: Perfect number is a positive integer that is equal to the sum of its proper divisors.
    The smallest perfect number is 6, which is the sum of 1, 2, and 3.
    Some other perfect numbers are 28(1+2+4+7+14=28), 496 and 8128.
    Write a function that finds perfect numbers between 1 and 1000. Check perfect numbers between 1 
    and 1000 and find the sum of the perfect numbers using reduce and filter functions.

"""

from functools import reduce

def perfect_numbers(number): 
   
   sum = 0
   for i in range(1,number):
      if number%i == 0:
         sum += i
   return sum == number # The loop is exited when the divisors of the number are equal to the number.
list1 = list(filter(perfect_numbers,range(1,1000))) # Created a list of Perfect Numbers
print(list1)
sum_list = reduce(lambda x,y: x+y,list1) # The sum of the numbers is found with the reduce function
print(sum_list)