'''
Developer   : Musab SARI
Date        : 25.01.2023

Question 3:
Write a program that list according to email addresses without email domains in a text.

Example:

Input:

The advencements in biomarine studies franky@google.com with the investments necessary and Davos sinatra123@yahoo.com. Then New Yorker article on wind farms...

Output :

franky

sinatra123

'''

import re

emaildomain = re.compile(r'(\S+)[@]\w+[.]com\b')

usertextinput = input('Text: ')

for i in emaildomain.findall(usertextinput):
    print(i)

### Well done!!!