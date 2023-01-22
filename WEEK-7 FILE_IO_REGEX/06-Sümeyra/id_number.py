
#Write a program that detects the ID number hidden in a text. 
#We know that the format of the ID number is 2 letters, 1 digit, 2 letters, 2 digits, 1 letter, 1 digit (For example: AA4ZA11B1).

#Input : AABZA1111AEGTV5YH678MK4FM53B6
#Output : MK4FM53B6
#Input : AEGTV5VZ4PF94B6YH678
#Output : VZ4PF94B6


import re

text1 = "AABZA1111AEGTV5YH678MK4FM53B6"
print(re.findall("\D{2}\d\D{2}\d{2}\D", text1))

text2 = "AEGTV5VZ4PF94B6YH678"
print(re.findall("\D{2}\d\D{2}\d{2}\D", text2))