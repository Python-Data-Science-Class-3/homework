""" 

Write a python script that shows the result by taking the date and currency types from the user to learn from the api site below. 
You can find the currency symbols on the api site. api site: https://www.exchangerate-api.com/

For example, when the user wants to learn the USD/TRY exchange rate at 15/01/2023, the result is : "1 USD is 18.7872 TRY on 15/01/2023."
If you want you can use try-except to prevent the incorrect inputs.



"""




import requests
from tkinter import *
def currency_history(Convert_currency,Currency_Type,year,Month,Day):

    apiKey = 'f86fa9769c21f91e9ecdf13b'
   
    url = f"https://v6.exchangerate-api.com/v6/{apiKey}/history/{Currency_Type}/{year}/{Month}/{Day}"

    response = requests.get(url)
    result = response.json()['conversion_rates'][Convert_currency]
    return (f'1 {Currency_Type} was {result} {Convert_currency} at {Day}/{Month}/{year} ...')





'''
Tkinter 


'''




root = Tk()     # opens a widget by using tkinter module


root.geometry("500x300+500+300") 

label = Label(root,text="Welcome to history of Currencies",font=("Comic Sans",15),fg ="black",bg="white")   # creates a label with a default text to greet user
label.place(relheight=10,
            relwidth=15
            )
label.pack()
'''
inputs from the user
'''
v = StringVar(root, value='currency')
inputtxt = Entry(root,width=20 ,textvariable=v )

inputtxt.pack()
inputtxt1 = Entry(root,width = 20)

inputtxt1.pack()
inputtxt2 = Entry(root, width = 20)
inputtxt2.pack()
inputtxt3 = Entry(root,width = 20)
inputtxt3.pack()
inputtxt4 = Entry(root,width = 20)
inputtxt4.pack()                                  

def convert():
    '''
    Calls our main fuction and writes the output to a label
    '''
    new_lb = Label(root , text=currency_history(inputtxt.get().upper(),inputtxt1.get().upper(),inputtxt2.get().upper(),inputtxt3.get().upper(),inputtxt4.get().upper()))
    new_lb.pack()

button = Button(root,                            # Creates a button------root is the window that we are going to use
                    text="CONVERT",             # Default text
                    command=convert,            # runs the convert function when clicked
                    font=("Comic Sans",20),     # Writing type and size
                    fg="#00FF00",               # forground color
                    bg="purple")                # background color
button.pack() 

label2 = Label(root , width=20, text= "1-Enter the first currency" ).place(x=365, y=26)
label3 = Label(root , width=20, text= "2-Enter the second currency" ).place(x=375, y=46)
label4 = Label(root , width=20, text= "3-Enter the Year" ).place(x=343, y=66)
label5 = Label(root , width=20, text= "4-Enter the Month" ).place(x=348, y=86)
label6 = Label(root , width=20, text= "5-Enter the day" ).place(x=340, y=106)



root.mainloop()


