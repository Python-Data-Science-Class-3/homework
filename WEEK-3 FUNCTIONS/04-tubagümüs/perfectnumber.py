'''Developer : Tuba GÜMÜS ESMEK
   Date      : 22.12.2022
   Subject   : Perfect Number

'''
#Perfect number: Perfect number is a positive integer that is equal to the sum of its proper divisors.
#The smallest perfect number is 6, which is the sum of 1, 2, and 3.
#Some other perfect numbers are 28(1+2+4+7+14=28), 496 and 8128.
#Write a function that finds perfect numbers between 1 and 1000. 
# #Check perfect numbers between 1 and 1000 and find the sum of the perfect numbers using reduce and filter functions.


from functools import  reduce

def diving_numbers(num):
    divisors = []

    sum = 0
    for i in range(1, num):
        if (num % i== 0):
            sum= sum+ i
            divisors.append(i)   #i +i/n

    return divisors

#print(diving_numbers())



a=diving_numbers (1000) 
#end  = reduce(filter(lambda x:+= sum//, a))
end = reduce(lambda b,c : b+c , a)
print(a)