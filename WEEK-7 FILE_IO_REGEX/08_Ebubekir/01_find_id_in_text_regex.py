"""Question 1:
Write a program that detects the ID number hidden in a text. 
We know that the format of the ID number is 2 letters, 1 digit, 2 letters, 2 digits, 1 letter, 1 digit (For example: AA4ZA11B1).

Input : AABZA1111AEGTV5YH678MK4FM53B6

Output : MK4FM53B6

Input : AEGTV5VZ4PF94B6YH678

Output : VZ4PF94B6"""

import re
input="AABZA1111AEGTV5YH678MK4FM53B6  AEGTV5VZ4PF94B6YH678   "


patern=r"\w{2}\d\w{2}\d\d\w\d"
#pattern=r"[a-zA-z]{2}\d[a-zA-z]{2}\d{2}[a-zA-z]\d"

a=re.findall(patern,input)
print(a)

b=re.search(patern,input)
print(b)



