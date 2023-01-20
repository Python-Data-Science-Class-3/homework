""" 

Developer : Melih Orhan Yilmaz
Date      : 18.01.2023

Application : Email addresses without email domains

Explanation : 
    Write a program that list according to email addresses without email domains in a text.
        Example:
        Input:
        The advencements in biomarine studies franky@google.com with the investments necessary and Davos sinatra123@yahoo.com. Then New Yorker 
        article on wind farms...
        Output :
        franky
        sinatra123

"""

import re

text =  "The advencements in biomarine studies franky@google.com with the investments necessary and Davos sinatra123@yahoo.com. Then New Yorker article on wind farms..."

find_email = re.findall(r"[\w\d\.-]+@\w+\.\w+",text)

print(find_email)

for i in find_email:
    no_domain = re.findall(r"[\w\d\.-]+",i)
    print(no_domain[0])