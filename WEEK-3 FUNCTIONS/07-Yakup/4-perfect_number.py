
#  Perfect number is a positive integer that is equal to the sum of its proper divisors.
# The smallest perfect number is 6, which is the sum of 1, 2, and 3.
# Some other perfect numbers are 28(1+2+4+7+14=28), 496 and 8128.
# Write a function that finds perfect numbers between 1 and 1000. 
# Check perfect numbers between 1 and 1000 and find the sum of the perfect numbers using reduce and filter functions.



def perfectNumber(p):
    
    sum =0
    for i in range(1,p):
       if (p % i ) == 0:
        sum+=i
    if (sum == p):
        result = "The number is a Perfect number!"
        return result
    else:
        result="The number is not a Perfect number!"
        return result


for n in range(1,1000):
   print (f'   {perfectNumber(n)}'     )



# items = [x for x in range(1,1000)]
# squared = list(filter(lambda x: x % 2 == 0, items))
# print(squared)