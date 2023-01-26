'''
Developer   : Musab SARI
Date        : 25.01.2023

Question 1:
Write a program that detects the ID number hidden in a text. We know that the format of the ID number is 2 letters, 1 digit, 2 letters, 2 digits, 1 letter, 1 digit (For example: AA4ZA11B1).

Input : AABZA1111AEGTV5YH678MK4FM53B6

Output : MK4FM53B6

Input : AEGTV5VZ4PF94B6YH678

Output : VZ4PF94B6

'''

import re

idnumberregex = re.compile(r'[a-zA-Z]{2}\d[a-zA-Z]{2}\d{2}[a-zA-Z]\d')

user_input = input("Enter the text to be searched for ID number in it: ")

print(idnumberregex.findall(user_input))