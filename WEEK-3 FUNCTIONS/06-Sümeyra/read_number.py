#Write a function that outputs the transcription of an input number with two digits.
#Example:
#28---------------->Twenty Eight

def read_number():
    ones_digit = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "ninteen"]
    tens_digit = ["", "ten", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninty"]
    
    number = input("Enter a number:")
    
    if int(number[0]) == 1:
        print(tens[int(number[1])])

    else:  # from 20 to 99 not have a special name.First part is first number, second part is second number
        print(tens_digit[int(number[0])],ones_digit[int(number[1])])
        
read_number()

'''
Gayet basarili, tebrikler.
'''