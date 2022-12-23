""" 

Developer : Melih Orhan Yilmaz
Date      : 22.12.2022

Application : Reading Numbers

Explanation : 
    Write a function that outputs the transcription of an input number with two digits.
    Example:
    28---------------->Twenty Eight

"""

i = int(input("Write a number 1 to 100: "))

def reading_numbers(number):

    # The reason for putting empty elements at the beginning of the list is that the number and the index in the list are the same.
    ones = ('', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', \
            'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen')
    tens = ('', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety')


    if 1<=number<=19: # Since the numbers between 1 and 20 are spelled differently, a separate list is created.
        return  ones[number] # List ones[index]

    elif 19<number<100:
        return  tens[number // 10]  + ones[int(number % 10)] # List tens[index] + Remainder of dividing a number by 10, ones[index]

    else:
        return "Out of Range"

print(reading_numbers(i))

