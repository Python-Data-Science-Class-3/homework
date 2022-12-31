"""
Author: Adem DOĞAN

Subject of the Program :Random Password As a user, I want to use a program which can
generate random password and display the result on user interface. So that I can generate
my password for any application.

Date :12/2022
"""

import tkinter as tk
import random 

form = tk.Tk()
form.title = ("Random Password")
form.geometry('400x400+50+100')
alphabet = "abcdefghijklmnopqrstuvwxyz"
b_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
s_char = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
liste = random.sample(s_char,2)+random.sample(alphabet,4)+random.sample(b_alphabet,2)+random.sample(numbers,2)

def show_result():
    label.config(text = liste,fg="white", bg="red")

label= tk.Label(form,fg="yellow", bg="blue",font = "Arial 30 italic bold")
label.pack()
result=tk.Button(form,text = "Click for Password", fg="black", bg="yellow",font = "Times 30 italic bold", command=show_result)
show_result.pack()

form.mainloop()

### I couldn't run the program.
### Traceback (most recent call last):
### File "d:\workspace\mentor\WEEK-4 MODULES\12-Adem\Random_Password.py", line 29, in <module>
### show_result.pack()
### AttributeError: 'function' object has no attribute 'pack'
### Let's evaluate the error code, fix it again and resend it.