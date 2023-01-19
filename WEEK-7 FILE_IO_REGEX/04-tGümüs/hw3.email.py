""" Developer : Tuba Gümüs Esmek
    Date      : 19.01.2023
    Subject   : Email Addresses without Email Domains
"""

# Write a program that list according to email addresses without email domains in a text.

# Example:

# Input:
# The advencements in biomarine studies franky@google.com with the investments necessary and Davos sinatra123@yahoo.com. 
# Then New Yorker article on wind farms...

# Output :
# franky
# sinatra123

import re     # importing regex
text = """
The advencements in biomarine studies franky@google.com with the investments necessary and 
Davos sinatra123@yahoo.com.Then New Yorker article on wind farms..."""

#Email addresses that are not email domains were created
e_mail = re.findall("([a-z]{1,}\w+)@", text)
print(e_mail)
