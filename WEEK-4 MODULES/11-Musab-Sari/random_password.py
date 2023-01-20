'''
Developer   : Musab SARI
Date        : 01.01.2023

Application : Random Password

Explanation : Random password is an application where user can generate 10 characters long random passwords just by clicking "Generate" button.
'''

import tkinter as tk
import string
import random

character_list = list(string.ascii_letters + string.digits + string.punctuation)

def password_generate():
    
    x = []
    
    for i in range(2):
        
        i = random.choice(string.ascii_uppercase)
        x.append(i)
    
    for i in range(2):
        
        i = random.choice(string.digits)
        x.append(i)
    
    for i in range(2):
       
        i = random.choice(string.punctuation)
        x.append(i)
    
    for i in range(4):
        
        i = random.choice(character_list)
        x.append(i)
        random.shuffle(x)
    
    return print(''.join(x))

pw = tk.Tk()

label = tk.Label(pw, text='Password Generator', font=('Arial', 18))
label.pack(padx=10, pady=10)

button_generate = tk.Button(pw, text='Generate', font=('Arial', 16),command = password_generate)
button_generate.pack(padx=20, pady=20)

pw.mainloop()