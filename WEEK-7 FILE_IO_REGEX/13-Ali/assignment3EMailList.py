# Question 3:
# Write a program that list according to email addresses without email domains in a text.

# Example:

# Input:
# The advencements in biomarine studies franky@google.com with the investments necessary and Davos sinatra123@yahoo.com. Then New Yorker article on wind farms...

# Output :
# franky
# sinatra123
import re
mailanchors = re.compile(r'[a-zA-Z0-9*+-_.]+\@[a-zA-Z0-9*+-_.]+\.[a-zA-Z0-9*+-_.]+') 
split = re.compile(r'''            # in this step the e-mail adresse are being separated as name, domain like "gmail" and the part like "com" after domain 
    (^[a-zA-Z0-9*+-_.]+)
    @
    ([a-zA-Z0-9*+-_.]+)
    \.
    ([a-zA-Z0-9*+-_.]+)
''',re.VERBOSE)                                    

mailVerbose = mailanchors.findall('The advencements in biomarine studies franky@google.com with the investments necessary and Davos sinatra123@yahoo.com. Then New Yorker article on wind farms...')


# print(mailVerbose) 
ultimateList = []                  #here the e-mail adress separated are being compiled in tuples nested in a list
for i in mailVerbose:    
    b = split.search(i)
    ultimateList.append(b.groups())      
   
print(list(item[0] for item in ultimateList))    # the target part name (before "@") is being picked here
