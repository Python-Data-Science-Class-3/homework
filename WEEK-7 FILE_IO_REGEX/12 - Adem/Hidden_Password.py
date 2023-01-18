"""
Author: Adem DOĞAN

Write a program that detects the ID number hidden in a text. We know that the format of the ID number is 2 letters,
1 digit, 2 letters, 2 digits, 1 letter, 1 digit.(For example: AA4ZA11B1). 

Date :1/2023
"""

import re

while True:
    string = str(input("Enter the text"))
    print(string)

    choice = str(input("The text you entered is on the screen. Press C to continue, press T to enter text again.")).upper()

    if choice == "C":
        pattern = '\w{2}\d\w{2}\d{2}\w\d'
        result = re.findall(pattern, string) 
        if result ==[]:
            print("There is no password in the text")
            break
        else:
            print(result)
            break

    elif choice == "T":
        continue
    
    else:
        print("It shouldn't be that hard to press C or T !!!!!")
        break