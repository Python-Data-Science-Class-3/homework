'''
Question 1:
Write a program that detects the ID number hidden in a text. We know that the format of the ID number is
 2 letters, 1 digit, 2 letters, 2 digits, 1 letter, 1 digit (For example: AA4ZA11B1).

Input : AABZA1111AEGTV5YH678MK4FM53B6

Output : MK4FM53B6

Input : AEGTV5VZ4PF94B6YH678

Output : VZ4PF94B6
'''
import re 

message = 'AABZA1111AEGTV5YH678MK4FM53B6'
'''
this is old method
'''
def oldmethod(message):
    for i in range(len(message)):
        if not message[i].isdecimal() and not message[i+1].isdecimal() and  message[i+2].isdecimal() and not message[i+3].isdecimal() and  not message[i+4].isdecimal() and  message[i+5].isdecimal() and  message[i+6].isdecimal() and not  message[i+7].isdecimal() and  message[i+8].isdecimal():
            print(message[i:i+9])
        
def newmethod(message):
    ID_regex = re.compile(r'[A-Z]{2}\d[A-Z]{2}\d{2}[A-Z]\d')   #If text includes nondigit and nonword chars
    # ID_regex = re.compile(r'\w{2}\d\w{2}\d{2}\w\d') # This is enough for the given text

    ID = ID_regex.search(message)
    if ID:
        print(ID.group())

oldmethod(message)
newmethod(message)