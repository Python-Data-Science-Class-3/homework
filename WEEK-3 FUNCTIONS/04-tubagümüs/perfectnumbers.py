'''Developer : Tuba GÜMÜS ESMEK
   Date      : 22.12.2022
   Subject   : Perfect Number

'''
#Perfect number: Perfect number is a positive integer that is equal to the sum of its proper divisors.
#The smallest perfect number is 6, which is the sum of 1, 2, and 3.
#Some other perfect numbers are 28(1+2+4+7+14=28), 496 and 8128.
#Write a function that finds perfect numbers between 1 and 1000. 
# #Check perfect numbers between 1 and 1000 and find the sum of the perfect numbers using reduce and filter functions.


def diving_numbers(num):  #creating the function
    divisors = []         # list to write numbers
    for i in range(1, num+1):    #set it from 1 to number we want with the for loop
        sum = 0                 #define the total value and set it to 0
        for j in range(1,i):     #creating a new loop
            if (i % j== 0):      #divisors of a number
                sum= sum+ j #the sum of the divisors of the number
        if sum==i:            #equalize the sum of the divisors of a number to a number with if loop
            divisors.append(i)
          
    return divisors
print(diving_numbers(1000)) 