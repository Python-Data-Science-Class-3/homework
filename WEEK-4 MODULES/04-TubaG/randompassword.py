'''Devoloper : Tuba GÜMÜS ESMEK
   Date      : 29.12.2022
   Subjeckt  : Random Password

'''

# - Random Password

#As a user, I want to use a program which can generate random password and display the result on user interface. 
# #So that I can generate my password for any application.

#Acceptance Criteria:

#Password length must be 10 characters long. #
# It must contain at least 2 upper case letter, 2 digits and 2 special symbols.
#  You must import some required modules or packages. 
# The GUI of program must contain at least a button and a label. 
# The result should be display on the password label when the user click the generate button. 
#(use import random, string and tkinter)

from tkinter import *       #tkinter,,string, ramdom importing
from tkinter import ttk
import  string as s 
import random as r
from random import randint


def random_password():    #function definitionn for printing password in tkinter
       pass
       
 # determinig password characters and creating random password     
       characters = r.sample(s.digits,2)+ r.sample(s.punctuation,2)+r.sample(s.ascii_uppercase,2)+r.sample(s.ascii_letters,4)
       password = "".join(r.sample(characters,10))  #for x in range (randint(10)) )
       print(password)
       tag.config(text=password)     #transferring the password output to GUI
  
#program GUI and steps to create Button and Label   
window = Tk()
window.title("infotechakademia_Datascience_Login")
#window.geometry("600*400")
window.config(bg="pink")
key_application = Frame(window)
key_application.pack()

tag = Label(window)
tag.config(text="Welcome,Please push the Botton",font = "arial 12")
tag.pack(padx= 90, pady= 30)


tag_1 = Label(window)
tag_1.config(text ="Password:" )
tag_1.pack()


button1 =Button(window,text="RANDOM PASSWORD", bg= "purple", command=random_password)
button1.pack()


button2 = Button(window,text="Sign out", command= window.destroy) #Password exit button
button2.pack(pady= 40)

mainloop()