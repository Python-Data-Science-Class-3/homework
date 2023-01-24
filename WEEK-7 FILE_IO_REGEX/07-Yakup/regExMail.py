"""
Question 3:
Write a program that list according to email addresses without email domains in a text.

Example:

Input:
The advencements in biomarine studies franky@google.com 
with the investments necessary and Davos sinatra123@yahoo.com. 
Then New Yorker article on wind farms...

Output :
franky
sinatra123

""" 

import re

pattern = r"(\w+)@"

txt=''' The advencements in biomarine studies franky@google.com 
with the investments necessary and Davos sinatra123@yahoo.com. 
Then New Yorker article on wind farms...'''

mo=re.findall(pattern,txt)
for i in mo:
    print()
    print(i)
    print()
   
