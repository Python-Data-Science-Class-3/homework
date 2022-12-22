def perfect_number(number):
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum += i
    return sum == number
perfect_numbers = filter(perfect_number, range(1, 1001))
print('Perfect numbers between 1 and 1000:', list(perfect_numbers))

from functools import reduce
print('Sum of perfect numbers between 1 and 1000:', reduce(lambda x, y: x + y, filter(perfect_number, range(1, 1001))))