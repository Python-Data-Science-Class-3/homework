"""
Author: Adem DOĞAN

Write a program that list according to email addresses without email domains in a text.

Date :1/2023
"""
import re

s = """The advencements in biomarine studies franky@google.com with the investments necessary 
and Davos sinatra123@yahoo.com. Then New Yorker article on wind farms..."""

s = re.findall('\w+(?=[@])', s)

print (s)

### Well done!!!