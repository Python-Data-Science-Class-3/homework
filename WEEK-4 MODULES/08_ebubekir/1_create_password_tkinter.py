"""1 - Random Password As a user, I want to use a program which can generate random password and display the result on user interface. 
So that I can generate my password for any application.

Acceptance Criteria: Password length must be 10 characters long.
It must contain at least 2 upper case letter, 2 digits and 2 special symbols.
You must import some required modules or packages. The GUI of program must contain at least a button and a label.
The result should be display on the password label when the user click the generate button. (use import random, string and tkinter)"""

from tkinter import *
from random import randint
window=Tk()
window.title("Strong Password Generator:")
window.iconbitmap()
window.geometry("500x300")

def new_pas():
    #clear entry box
    pw_entry.delete(0,END)
    #get pw length and convert to integer
    pw_length=int(my_entry.get())
    #create a variable to hold our password
    my_password=''
    #loop through password length
    for x in range(pw_length):
        my_password+=chr(randint(33,126))
        #output password to the screen
        pw_entry.insert(0,my_password)
#Label Frame
lf=LabelFrame(window,text="How many characters?")
lf.pack(pady=20)
# Create entry box to designate
my_entry=Entry(lf,font=("verdana",24))
my_entry.pack(padx=20,pady=20)
#Create entry box for our reurnede password
pw_entry=Entry(window,text='',font=("verdana",20),bg="yellow")
pw_entry.pack(pady=20)
#Create a frame for our buttons
my_frame=Frame(window)
my_frame.pack(pady=20)
#Create our buttons
my_button=Button(my_frame,text="Generate Strong Password",command=new_pas)
my_button.grid(row=0,column=1,padx=10)

window.mainloop()
