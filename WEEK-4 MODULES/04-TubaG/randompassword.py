'''Devoloper : Tuba GÜMÜS ESMEK
   Date      : 29.12.2022
   Subjeckt  : Random Password

'''

# - Random Password

#As a user, I want to use a program which can generate random password and display the result on user interface. 
# #So that I can generate my password for any application.

#Acceptance Criteria:

#Password length must be 10 characters long. #
# It must contain at least 2 upper case letter, 2 digits and 2 special symbols.
# # You must import some required modules or packages. 
# #The GUI of program must contain at least a button and a label. 
# The result should be display on the password label when the user click the generate button. 
#(use import random, string and tkinter)

import  string as s 

#print(s.ascii_letters)
print(s.ascii_lowercase)
print(s.ascii_uppercase)
print(s.digits)
print(s.punctuation)

import random as r

password =str(s.digits+ s.ascii_letters + s.punctuation)
#password = s.digits + s.ascii_letters + s.punctuation
#password = r.sample(list((s.ascii_lowercase,2) +(s.ascii_uppercase,4)+ (s.digits,2)+(s.punctuation,2)))

print("".join(r.sample(password, 10)))


from tkinter import *
from tkinter import ttk


window = Tk()
window.title( "infotechakademia_Datascience")
window.geometry("400x450")
window.config(bg= "pink")

tag = Label(window)
tag =Label(window, text ="write password",bg ="pink", font = "arial 20",width = 30, height = 20)
tag.pack

entry = Entry(window)
entry.place(x=30, y=30)


button1 = Button(window, text = "sign in", bg="black")
button1.pack()
button2 = Button(window, text ="Sign out", command =window.destroy)
button2.pack(pady =50)


window.mainloop()