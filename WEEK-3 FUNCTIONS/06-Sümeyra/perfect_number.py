# Perfect number: Perfect number is a positive integer that is equal to the sum of its proper divisors.
# The smallest perfect number is 6, which is the sum of 1, 2, and 3.
# Some other perfect numbers are 28(1+2+4+7+14=28), 496 and 8128.
# Write a function that finds perfect numbers between 1 and 1000. Check perfect numbers between 1 and 1000 and find the sum of the perfect numbers using reduce and filter functions.

def perfect_number(n):  # user-defined function
   
   sum = 0
   for i in range(1, n):
      if n%i == 0:
         sum += i
   return sum == n
filter1 = list(filter(perfect_number, range(1, 1000)))

print("Perfect numbers between 1 and 1000:", filter1)  # calling function and print perfect numbers

'''
Gayet guzel, bir de 'reduce' metodunu kullanarak bu sayilari toplayip yazdiralim.
Bizden istenen bunu da kullanip toplamini bulmak.
'''