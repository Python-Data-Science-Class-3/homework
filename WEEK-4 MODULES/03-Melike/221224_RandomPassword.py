"""
1 - Random Password 
As a user, I want to use a program which can generate random password and display the result on user interface. 
So that I can generate my password for any application.

Acceptance Criteria: 

Password length must be 10 characters long. 
It must contain at least 2 upper case letter, 2 digits and 2 special symbols. 
You must import some required modules or packages. 

The GUI of program must contain at least a button and a label. 
The result should be display on the password label when the user click the generate button. 
(use import random, string and tkinter)
"""

### It always seems to return the same password everytime we try a new round
### The password moves outside the table, can you fix that too?
### You can use the "string" module to pull all characters


import random
from tkinter import *

a = "abcdefghijklmnopqrstuvwxyz"
b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
c = "1234567890"
d = "!'+%&/()=?,.@"

x = "".join(random.sample(a,4))+"".join(random.sample(b,2))+"".join(random.sample(c,2))+"".join(random.sample(d,2))
password = "".join(random.sample(x,10))

def run():
    new_password = Label(text= f"New password is generated:\n {password}", fg="#0e4669", font= ("Monaco", 26))
    new_password.pack()

root = Tk()

root.geometry("500x300")
root.title("Random Password")

myLabel = Label(root, text="PASSWORD", fg="#365deb", font= ("Monaco", 18))
myLabel.pack(padx=20, pady=20)

second_label = Label(root, text="Welcome to the Random Password Generator!", fg="#69140e", font= ("San Francisco", 12))
second_label.pack()

button = Button(root, text= "GENERATE!", fg="#345eeb", bg="#6b86e3", font= ("Menlo", 24), command=run)
button.pack(padx=20, pady=20)

root.mainloop()