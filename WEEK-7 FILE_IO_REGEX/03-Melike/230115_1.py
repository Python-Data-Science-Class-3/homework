"""
Question 1:

Write a program that detects the ID number hidden in a text. 
We know that the format of the ID number is 2 letters, 1 digit, 
2 letters, 2 digits, 1 letter, 1 digit (For example: AA4ZA11B1).

Input : AABZA1111AEGTV5YH678MK4FM53B6
Output : MK4FM53B6

Input : AEGTV5VZ4PF94B6YH678
Output : VZ4PF94B6
"""

import re 

text = input ("Please input the text here: ")

id_number_finder = re.compile(r"[A-Z]{2}\d{1}[A-Z]{2}\d{2}[A-Z]{1}\d{1}")
ID = id_number_finder.search(text)

print(ID.group())