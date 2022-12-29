#Random Password
#As a user, I want to use a program which can generate random password and display the result on user interface. 
#So that I can generate my password for any application.

#Acceptance Criteria:
#Password length must be 10 characters long. 
#It must contain at least 2 upper case letter, 2 digits and 2 special symbols.
#You must import some required modules or packages. 
#The GUI of program must contain at least a button and a label. 
# The result should be display on the password label when the user click the generate button.(use import random, string and tkinter)


import string,random
import tkinter as t

def random_password():
    length = 10 #password length
    uppers = string.ascii_uppercase 
    lowers = string.ascii_lowercase
    digits = string.digits 
    punctuation = string.punctuation
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation  #combining all ascii letters, digits and punctuations
    lower = ''.join(random.choice(lowers) for i in range(2)) #contain at least 2 upper,lower case letter, 2 digits and 2 punctuations.
    upper = ''.join(random.choice(uppers) for i in range(2))
    digit = ''.join(random.choice(digits) for i in range(2))
    punc= ''.join(random.choice(punctuation) for i in range(2))
    password = lower + upper + digit + punc +''.join(random.choice(chars) for i in range(length-8)) 
    r_password = ''.join(random.sample(password,len(password))) #shuffle and return
    label.config(text=r_password)
    return r_password 


window=t.Tk()
window.title("Password  Generator")
window.geometry("800x400")
frame = t.Frame(window)
frame.grid()

label_text = t.Label(frame, text="Password: ",font="sans 20")
label_text.grid(padx = 70, pady = 20)

label = t.Label(frame, text ="Click the button to generate a password",font="sans 16",fg="red" )
label.grid(padx = 70, pady = 20)


button = t.Button(frame,text="Click to Generate",font="sans20",width= 70, height=7,command=random_password)
button.grid(padx =10 , pady = 20)

window.mainloop()
