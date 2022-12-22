""" 
5-reading_number.py
Write a function that outputs the transcription of an input number with two digits.
Example:
28---------------->Twenty Eight""" 

digits = {0: "", 1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine", 
11:"Eleven", 12:"Twelve", 13:"Thirteen", 15: "Fifteen",
10:"Ten", 20:"Twenty", 30:"Thirty", 40:"Forty", 50:"Fifty", 60:"Sixty", 70:"Seventy", 80:"Eighty", 90:"Ninety"}

def reading_number(num):
    if 99 > num > 19:
        print(f"{digits[num-num%10]} {digits[num%10]}")         # to find ten_digit of number, the modulus by ten is substracted
    elif num in [14,16,17,18,19]:
        print(f"{digits[num%10]}teen")
    elif num in [10,11,12,13,15]:
        print(f"{digits[num]}")
    else:
        print("Please input another number..")
    

reading_number(28)
