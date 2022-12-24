## 4-perfect_number.py

# Perfect number: Perfect number is a positive integer that is equal to the sum of its proper divisors.
# The smallest perfect number is 6, which is the sum of 1, 2, and 3.
# Some other perfect numbers are 28(1+2+4+7+14=28), 496 and 8128.
# Write a function that finds perfect numbers between 1 and 1000. Check perfect numbers between 1 and 1000 and find the sum of the perfect numbers using reduce and filter functions.

#-----------------Made by Yunus Donmez--------------21/12/2022
def super_number():
    '''
    This is function finds super numbers

    '''
    b=0
    for i in range(1,1000):     # Loop for every item till 1000
        for j in range(1,i):    # Loop fo every item till 'i' value
            if (i)%(j)==0 and i != j :     # Checks if i is divisible withour remainder by j and we dont count division by itself
                b=b+j           # Sums every divisor
                
        if b==i :               # Checks if the sums of divisor is equal to number itself
            print(b)
        b = 0                   # IF its not true for the given 'i' number , we reset the b value for the next 'i' value in loop
super_number()