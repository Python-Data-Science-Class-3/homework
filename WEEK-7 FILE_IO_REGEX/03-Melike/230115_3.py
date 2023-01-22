"""
Question 3:
Write a program that list according to email addresses without email domains in a text.

Example:
Input:
The advencements in biomarine studies franky@google.com with the investments necessary and Davos sinatra123@yahoo.com. 
Then New Yorker article on wind farms...

Output :
franky
sinatra123"""

import re

text = input("Please input a text here: ")

mail_finder = re.compile(r"(\S+)@\S+.com")
for i in mail_finder.findall(text):
    print(i)