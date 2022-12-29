import tkinter as tk
import string
from random import *
box=tk.Tk()
box.geometry("500x100")
box.title("Creat a Password")

def password():
    characters = string.ascii_letters + string.punctuation + string.digits
    password0 = "".join(choice(characters) for x in range(randint(10, 11)))
    x=(f"password = {password0}")
    write.config(text=x)

write=tk.Label(box, text="Click button Please")
write.pack()

button=tk.Button(box, text="button", command=password)
button.pack()

button=tk.Button(box, text="Exit", command=exit)
button.pack()
box.mainloop()