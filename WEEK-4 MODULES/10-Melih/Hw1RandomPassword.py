""" 

Developer : Melih Orhan Yilmaz
Date      : 26.12.2022

Application : Random Password

Explanation : 
    As a user, I want to use a program which can generate random password and display the result on user interface. 
    So that I can generate my password for any application.

    Acceptance Criteria:
    Password length must be 10 characters long. It must contain at least 2 upper case letter, 2 digits and 2 special
    symbols. You must import some required modules or packages. The GUI of program must contain at least a button 
    and a label. The result should be display on the password label when the user click the generate button. 
    (use import random, string and tkinter)

"""

import random,string
import tkinter as tk

print("Welcome")

length = 10

def characters():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digit = string.digits
    symbol = string.punctuation
    all_characters = lower + upper + digit + symbol

    password = []
    password.append(random.choice(upper))
    password.append(random.choice(digit))
    password.append(random.choice(symbol))
    password.append(random.choice(upper))
    password.append(random.choice(digit))
    password.append(random.choice(symbol))
    for i in range(1, length - 5):
        if len(password) < length:
            password.append(random.choice(all_characters))

    random.shuffle(password) # Shuffle the password list to randomize it
    random_password = ''.join(password)     # Concatenate the individual characters in the password list into a string with the join function.


    return random_password

print("Password: ",characters())

"""
# I couldn't make 'at least 2' constraint

def generate_password():
    password = "".join(random.sample(characters(), length))
    return password

print("Password: ", generate_password())
"""

#Hocam burada generate'e bastığımda neden password'u vermiyor anlamadım. Print yazdırıyor ama tkinter ile yapamadım.
top = tk.Tk()  

top.title("PASSWORD")
top.geometry("300x300") 

label = tk.Label(top, text = "Please click the button for random password", font=('Arial', 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(top, height=3, font=('Arial',16))
textbox.pack(padx=10)

submit_button = tk.Button(top,text = "Generate",font=('Arial',18), command=characters)
submit_button.pack()

top.mainloop()