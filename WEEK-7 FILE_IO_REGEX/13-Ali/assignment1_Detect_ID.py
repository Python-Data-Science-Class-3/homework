# Question 1:
# Write a program that detects the ID number hidden in a text. 
# We know that the format of the ID number is 2 letters, 1 digit, 2 letters, 2 digits, 1 letter, 1 digit (For example: AA4ZA11B1).

# Input : AABZA1111AEGTV5YH678MK4FM53B6

# Output : MK4FM53B6

# Input : AEGTV5VZ4PF94B6YH678

# Output : VZ4PF94B6

import re
Data = input("enter text to detect ID in it: ")          
Inquiry = re.compile("[A-Z]{2}[0-9][A-Z]{2}[0-9]{2}[A-Z][0-9]")
Outcome = Inquiry.search(Data)
print(Outcome.group())

