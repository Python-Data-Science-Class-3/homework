"""Question 3:
Write a program that list according to email addresses without email domains in a text.

Example:

Input:

The advencements in biomarine studies franky@google.com with the investments necessary and Davos sinatra123@yahoo.com.
 Then New Yorker article on wind farms...

Output :

franky

sinatra123"""

import re
input="The advencements in biomarine studies franky@google.com with the investments necessary and Davos sinatra123@yahoo.com. Then New Yorker article on wind farms..."

pattern=r"(\w{1,}|\d)@"
#pattern=r"(([a-zA-Z0-9.-]+)@[a-zA-z0-9-]+\.(com|edu|net))"
a=re.findall(pattern,input)
print(a)