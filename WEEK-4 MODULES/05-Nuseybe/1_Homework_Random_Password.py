#Random Password
# As a user, I want to use a program which can generate random password and display the result on user interface. 
# So that I can generate my password for any application.
# Acceptance Criteria:
# Password length must be 10 characters long. It must contain at least 2 upper case letter, 2 digits and 2 special symbols. 
# You must import some required modules or packages. The GUI of program must contain at least a button and a label. 
# The result should be display on the password label when the user click the generate button. (use import random, string and tkinter)
#written by Nuseybe at 28.12.2022


import tkinter as tk

window = tk.Tk()                                                     # creating a window with tkinter
window.title("Generate Password")                                    # window's title
window.geometry("400x400")                                           #window's size
text=tk.Label(window,text="Click for generate ", font=16)            # create a label for info
text.pack()

l1=tk.Label(window,text="When you click the button your password seem here",font=16)            #an information about button 
l1.pack()

import string
import random

def generate_password(length=10):
    two_random_uppercase = random.choices(string.ascii_uppercase, k=2)                          #to password at least 2 uppercases are adding
    two_random_lowercase = random.choices(string.ascii_lowercase, k=2)                          #to password at least 2 lowercases are adding 
    two_random_characters = random.choices(string.punctuation, k=2)                             #to password at least 2 spaecial characters are adding
    other_random_digits = random.choices( string.digits, k=length - 6)                          #The remaining characters of the password, which is 10 characters in total, are numbers. 
    password = "".join(random.sample(two_random_uppercase + other_random_digits + two_random_characters+ two_random_lowercase, k=length))        #joining all characters for password
    l1.configure(text=password)                                                                                                                  #password is showing in the window
    return password
#print(generate_password())



button=tk.Button(window,text="Generate", padx=50, pady=25,font=16,  command = generate_password)                #creating a button command in the window  for function 
button.place(x=20 , y=60)


window.mainloop()                                                                                               # keeps the window open until the user closes it