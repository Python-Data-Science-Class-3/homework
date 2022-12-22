
'''
Write a function that outputs the transcription of an input number with two digits.

Example:

28---------------->Twenty Eight
'''




first_digit = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
second_digit = ["", "Ten", "Twenty", "Thirty", "Fourty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninty"]
def read_numbers(numbers):

    a = numbers // 10
    b = numbers % 10
    return second_digit [a] + first_digit[b]


numbers=int(input("Please enter a two digit number:"))
print("Your number is:" ,read_numbers(numbers))