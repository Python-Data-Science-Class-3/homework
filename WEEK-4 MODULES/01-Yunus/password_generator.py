# 1 - Random Password As a user, I want to use a program which can generate random password 
# and display the result on user interface. So that I can generate my password for any application.

# Acceptance Criteria: Password length must be 10 characters long. It must contain at least 2 upper 
# case letter, 2 digits and 2 special symbols. You must import some required modules or packages.
# The GUI of program must contain at least a button and a label. The result should be display on the 
# password label when the user click the generate button. (use import random, string and tkinter)

#-----------Made by Yunus Donmez 25/12/2022--------------
import random                   #Importing required packages and modules
import string
import tkinter as tk


def password_generator(): 
    '''
    Generates password within acceptance Criteria
    '''
    final=''
    password = []
    for i in range(0,2):                                  # password should contain at least 2 number
        a = random.randint(0,len(string.digits)-1)        # generates a random number to be used as index
        password.append(string.digits[a])                 # Adds a number to our password by using string modules
    for i in range(0,2):
        a = random.randint(0,len(string.ascii_lowercase)-1)
        password.append(string.ascii_lowercase[a])        # Adds a lowercase to our password by using string modules
    for i in range(0,2):
        a = random.randint(0,len(string.ascii_uppercase)-1)
        password.append(string.ascii_uppercase[a])        # Adds a uppercase to our password by using string modules
    for i in range(0,2):
        a = random.randint(0,len(string.punctuation)-1)
        password.append(string.punctuation[a])            # Adds a special symbols to our password by using string modules
    for i in range(0,2):
        a = random.randint(0,len(string.ascii_letters+string.punctuation+string.digits)-1)
        password.append((string.ascii_letters+string.punctuation+string.digits)[a])         # Adds a random string to our password by using string modules
    random.shuffle(password)                                        # shuffle the list
    final = "".join(password)                                       # Converts the list to string
    label["text"] ="Password : "+final                                            # Changes the text in label
    


root = tk.Tk()     # opens a widget by using tkinter module

root.geometry("350x250") 

button = tk.Button(root,                        # Creates a button------root is the window that we are going to use
                    text="Generate",            # Default text
                    command=password_generator, # runs the password_generator when clicked
                    font=("Comic Sans",20),     # Writing type and size
                    fg="#00FF00",               # forground color
                    bg="purple")                # background color
button.pack()                                   

label2 = tk.Label(root,text="           ")   # creates a label with a default text to show generated password 
label2.pack()

label = tk.Label(root,text="hello",font=("Comic Sans",15),fg ="green",bg="yellow")   # creates a label with a default text to show generated password 
label.pack()
root.mainloop()