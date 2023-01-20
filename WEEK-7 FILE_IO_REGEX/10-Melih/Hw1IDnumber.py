""" 

Developer : Melih Orhan Yilmaz
Date      : 17.01.2023

Application : ID Number

Explanation : 
    Write a program that detects the ID number hidden in a text. We know that the format of the ID number is 2 letters, 1 digit, 2 letters, 
    2 digits, 1 letter, 1 digit (For example: AA4ZA11B1).
        Input : AABZA1111AEGTV5YH678MK4FM53B6
        Output : MK4FM53B6

        Input : AEGTV5VZ4PF94B6YH678
        Output : VZ4PF94B6

"""

import re
txt1 = 'AABZA1111AEGTV5YH678MK4FM53B6'
txt2 = 'AEGTV5VZ4PF94B6YH678'
id_number = re.compile(r'\w{2}\d{1}\w{2}\d{2}\w{1}\d{1}')
mo =id_number.search(txt1)
print(mo.group())