#Write a program that list according to email addresses without email domains in a text.
#Example:
#Input:
#The advencements in biomarine studies franky@google.com with the investments necessary and Davos sinatra123@yahoo.com. Then New Yorker article on wind farms...

import re

text = "The advencements in biomarine studies franky@google.com with the investments necessary and Davos sinatra123@yahoo.com"
print(re.findall("(\S+)@", text))


