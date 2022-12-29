'''1 - Random Password
As a user, I want to use a program which can generate random 
password and display the result on user interface. So that I 
can generate my password for any application.
Acceptance Criteria:
Password length must be 10 characters long. It must contain 
at least 2 upper case letter, 2 digits and 2 special symbols. 
You must import some required modules or packages. The GUI of 
program must contain at least a button and a label. The result 
should be display on the password label when the user click the
generate button. (use import random, string and tkinter)'''

import random
import string
from tkinter import *

# characters = string.printable
# print(characters)
# 0123456789
# abcdefghijklmnopqrstuvwxyz
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
#so far all the upper and lower alphanumeric and symbolic characters were determined via printable 

alphaLow = "abcdefghijklmnopqrstuvwxyz"
alphaUp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = '0123456789'
specialSymbols = "!#$%&()*+,-./:;<=>?@[]^_`{}~"
def generate():
    alphaLowChosen = random.choices(list(alphaLow), k = 4) # in this step characters  are chosen determined abowe 
    alphaUpChosen = random.choices(list(alphaUp), k = 2) # k show how many characters ise taken
    digitChosen = random.choices(list(digits), k = 2)
    speSymbolChosen = random.choices(list(specialSymbols), k = 2)

    concatall = speSymbolChosen+digitChosen+alphaLowChosen+alphaUpChosen #here ale characters chosen are gathered
    redistributeAll = random.sample(concatall, 10) # but 10 characters were in order chosen from their own group and here are again random chosen.

    strAll = ''.join(redistributeAll)
    return strAll
 
window = Tk()
window.geometry('450x150')
scrollbar = Scrollbar(window).pack(side=RIGHT, fill=Y)
   
def textCommand():
    global label
    label = Label(window, text= "new password: " + generate() ,
                        fg = "light pink",
                        bg = "black",
                        font = "Helvetica 16 bold italic",
                        justify= LEFT);label.pack(pady=5)        
def delete():
    label.destroy()
Button(window, text = "generate new password", command=textCommand).pack()
Button(window, text = "clear old password", command=delete ).pack()

window.mainloop()


    

