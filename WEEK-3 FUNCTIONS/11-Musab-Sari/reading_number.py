'''
Developer   : Musab SARI
Date        : 23.12.2022

Application : Reading Number

Explanation : Reading number is an application where you can enter numbers between 0-99 and can get an output exhibiting spelling of numbers in English
'''
a = int(input('Please enter your number between 0-99:'))

one_to_nineteen = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen',]
two_digit_numbers = ['Twenty','Thirty','Fourty','Fifty','Sixty','Seventy','Eighty','Nighty']

def reading_number(x):
    try:
        x is range(0,99)
        
        if x in range(0,20):
            print(x,'------>',one_to_nineteen[x])
        
        else:
            c = x // 10
            d = x % 10
            
            if d == 0:
                print(x,'------> ' f'{two_digit_numbers[c-2]}')
            else:
                print(x,'------> ' f'{two_digit_numbers[c-2]} {one_to_nineteen[d]}')

    except:
        print('Your number is out of range!')

reading_number(a)