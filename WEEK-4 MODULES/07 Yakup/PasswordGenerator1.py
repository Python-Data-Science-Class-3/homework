"""
As a user, I want to use a program which can generate random password and display
 the result on user interface. So that I can generate my password for any application.

Acceptance Criteria:

Password length must be 10 characters long. It must contain at least 2 upper case letter, 
2 digits and 2 special symbols. You must import some required modules or packages.
 The GUI of program must contain at least a button and a label. 
 The result should be display on the password label when the user click the generate button.
  (use import random, string and tkinter)
"""
import random 
from tkinter import *


mirror= Tk()
mirror.geometry("400x400")
mirror.title("Pass Genarotor")
mirror.configure(background ="bisque")
label =Label(mirror,text="My Password", background= 'bisque').pack()

def Password_Gen():
    global sc1
    sc1.set("")
    passw= random.choice(lowercase,k=2)
    
    lowercase='abcdefghijklmnopqrstuvwxyz'
    uppercase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    nums='0123456789'
    special = '@#$%&*'
        
    passwCodeBlok =[lowercase,uppercase,nums,special]
    for i in passwCodeBlok :
        passw=passw + random.choice(i,k=2)
    sc1.set(passw)

sc1=StringVar()
t1=Label(mirror,text='Password',font=('Arial',11),fg='green',background= 'bisque') 
t1.place(x=145,y=120) 

c1=Entry(mirror,font=('Arial',14),width=10)
c1.place(x=230,y=120)

b1=Button(mirror,text='Generate!',font=('Arial',14),fg='green',background ="gray",command=Password_Gen)
b1.place(x=130,y=195)

b2=Button(mirror,text='Exit',font=('Arial',14),fg='green',background ="gray",command=SystemExit)
b2.place(x=250,y=195)

mainloop()