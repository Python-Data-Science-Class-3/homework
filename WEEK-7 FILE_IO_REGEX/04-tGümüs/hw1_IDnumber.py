""" Developer : Tuba Gümüs Esmek
    Date      : 17.01.2023
    Subject   : ID Numbers
"""

# Write a program that detects the ID number hidden in a text. 
# We know that the format of the ID number is 2 letters, 1 digit, 2 letters, 2 digits, 1 letter, 1 digit 
# (For example: AA4ZA11B1).

# Input : AABZA1111AEGTV5YH678MK4FM53B6

# Output : MK4FM53B6

# Input : AEGTV5VZ4PF94B6YH678

# Output : VZ4PF94B6

import re       #importing regex
#A list of ID numbers has been created.
id_numbers = "AABZA1111AEGTV5YH678MK4FM53B6"  "AEGTV5VZ4PF94B6YH678"
#print(id_numbers)   # to check print list
#Formula written in desired format

id_num = re.findall(r"\D{2}\d\D{2}\d{2}\D", id_numbers)
for x in id_num:       #The process of printing the id numbers from the elements in the list with the for loop
    print(x)



"""
import re       #importing regex
id_number1 = "AABZA1111AEGTV5YH678MK4FM53B6"
id_number2 = "AEGTV5VZ4PF94B6YH678"


no1 = "\D{2}\d\D{2}\d{2}\D"
no2 = "\D{2}\d\D{2}\d{2}\D"
print(re.findall(no1, id_number1))
print(re.findall(no2, id_number2))

"""
