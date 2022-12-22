def reading_number(num):
    empty = ''
    x = [empty, 'One ', 'Two ', 'Three ', 'Four ', 'Five ', 'Six ', 'Seven ',
        'Eight ', 'Nine ', 'Ten ', 'Eleven ', 'Twelve ', 'Thirteen ', 'Fourteen ',
        'Fifteen ', 'Sixteen ', 'Seventeen ', 'Eighteen ', 'Nineteen ']
 
    y = [empty, empty, 'Twenty ', 'Thirty ', 'Forty ', 'Fifty ',
        'Sixty ', 'Seventy ', 'Eighty ', 'Ninety ']
   

    if (num < 20):
        return x[num]

    if (num < 100):
        return y[num // 10 ] + x[num % 10]
reading_number(25)