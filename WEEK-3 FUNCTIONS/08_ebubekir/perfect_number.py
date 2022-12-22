"""4-perfect_number.py
Perfect number: Perfect number is a positive integer t
hat is equal to the sum of its proper divisors.
The smallest perfect number is 6, which is the sum of 1, 2, and 3.
Some other perfect numbers are 28(1+2+4+7+14=28), 496 and 8128.
Write a function that finds perfect numbers between 1 and 1000. 
Check perfect numbers between 1 and 1000 and find the sum of the 
perfect numbers using reduce and filter functions.
"""

mukemmel = []
for i in range(1, 1001):
    bolen = []
    for j in range(1, i):
        if i % j == 0:
            bolen.append(j)
    if sum(bolen) == i:
        mukemmel.append(i)
print(mukemmel)