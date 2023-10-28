'''
   Developer : Tuba GÜMÜS ESMEK
   Date      : 22.12.2022
   Sukject   :Reading Number

'''
#Write a function that outputs the transcription of an input number with two digits.
#Example:
#28---------------->Twenty Eight


def reading_number (n):

    ones_digit = ["","one", "two","three", "four","five", "six","seven","eight", "nine", ] 
    #write  the numbers in the ones digit as a list
    tens_digit = ["","ten","eleven","twenty", "thirty","forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    ##write  the numbers in the tens digit as a list
    more_than_digit = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen","sixteen","seventeen","nineteen", ""]
    ones = n%10   #returns the reamining  from division of 10
    tens = n// 10 #the division gives the tens digit


    if 10 < n < 20:
        print(f"{n} ----------------> {more_than_digit[n - 10]}")
    else:
        print(f"{tens_digit[tens]} {ones_digit[ones]}")

new_number = int(input("write a number:\n"))
reading_number(new_number)



#     if (n//10==1):
#         print(f"\n{str(n)} ----------------> {more_than_digit[n%10]}")

#     else:
    
#        print(tens_digit[tens], ones_digit[ones]) #creating and printing  digits
#        ''' 
#        print(tens_digit[tens+1], ones_digit[ones])
        
#        tens_digit[tens+1] olmali. Yanlis sonucu veriyor. Calistirip kontrol edin.
#        '''

# new_number= int(input("write a number:\n"))
# reading_number(new_number)
