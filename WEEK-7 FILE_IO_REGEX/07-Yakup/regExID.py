""" 
Question 1:
Write a program that detects the ID number hidden in a text. 
We know that the format of the ID number is 
2 letters, 1 digit, 2 letters, 2 digits, 1 letter, 1 digit (For example: AA4ZA11B1).

Input : AABZA1111AEGTV5YH678MK4FM53B6

Output : MK4FM53B6

Input : AEGTV5VZ4PF94B6YH678

Output : VZ4PF94B6   
"""
import re
txt1= "AABZA1111AEGTV5YH678MK4FM53B6"

petter= r"\w{2}\d\w{2}\d{2}\w\d"
ID=re.search(petter,txt1)
print(ID.group())


txt2= input("Enter a text where your ID is hidden:")
petter2= r"\w{2}\d\w{2}\d{2}\w\d"
ID2=re.search(petter,txt2)
print(ID2.group())