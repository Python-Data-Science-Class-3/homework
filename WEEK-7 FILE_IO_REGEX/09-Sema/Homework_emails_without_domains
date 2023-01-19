#Homework Week 7
#Developer: Sema Sari
#Program Name: Emails without Domains
#Date: 19.01.2023



#Write a program that list according to email addresses without email domains in a text.

#Example:

#Input:

#The advencements in biomarine studies franky@google.com with the investments necessary and Davos sinatra123@yahoo.com. Then New Yorker article on wind farms...

#Output :

#franky

#sinatra123



import re
def email_domain(text):
    email_com=re.compile(r'([a-zA-Z0-9]+)(@)([a-zA-Z0-9]+)')
    usersname=[]
   
    for email in re.finditer(email_com,text):
     usersname.append(email.group(1))
    return usersname
text=input("Please enter a text that contains  email:")   
print(email_domain(text))    