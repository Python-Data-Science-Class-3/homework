# Write a function that outputs the transcription of an input number with two digits.
# Example:
# 28---------------->Twenty Eight

#-----------------Made by Yunus Donmez--------------21/12/2022
def reading_number():
    '''
    This function reads a given integer between 0 -99
    '''
    tens = ["ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
    numbers =["zero","one","two","three","four","five","six","seven","eight","nine"]
    teens = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]            
    while True:                             # In order to keep asking input
        n = input("Enter a number between 0-99 : \n")
        digit1 = int(n[0])                  #First digits of a given input
        if int(n)<10:                       #Checks if the number has only one digit
            print(f"{n}--------->{numbers[digit1]}")
        else :                              # if the number is bigger than 10 and therefore has two digits                            
            digit_2 = int(n[1])             # Second digit of given input

            if 10<int(n)<20:                # Numbers in between have uniq spelling
                print(f"{n}--------->{teens[digit_2]}")
            elif digit_2 == 0:              # if the number is orders of magnitude 10           
                print(f"{n}---------->{tens[digit1-1]}")
            else :                          # rest has no uniqe spelling
                print(f"{n}---------->{tens[digit1-1]} {numbers[digit_2]}")



reading_number()