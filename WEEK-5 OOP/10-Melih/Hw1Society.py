""" 

Developer : Melih Orhan Yilmaz
Date      : 05.01.2023

Application : Society OOP

Explanation : 
Create the class Society with following information:
society_name,house_no_of_mem, flat, income
Methods :
An __init__ method to assign initial values of society_name,house_no_of_mem, flat, income
input_data() To read information from members
allocate_flat() To allocate flat according to income using the below table.
show_data() to display the details of the entire class.
Income	            Flat
>=25000	            A Type
>=20000 and <25000	B Type
>=15000 and <20000	C Type
<15000	            D Type

"""

class Society():

    def __init__(self): # All the informations with valid default values
        self.society_name = ""
        self.house_no_of_mem = 0
        self.flat = ""
        self.income = 0


    def input_data(self): # Get input from the user
         while True:
            try:
                self.society_name = input("Enter Society Name: ") 
                self.house_no_of_mem=int(input("Enter Number of Members:")) 
                self.income = float(input("Enter Income: "))
                self.allocate_flat() # Call allocate_flat

                return self.society_name, self.house_no_of_mem, self.income

            except:
                print("Invalid. Please enter new value.")


    def allocate_flat(self):

        if self.income >= 25000:
            self.flat = "A Type"
        
        elif 25000 > self.income >= 20000:
            self.flat = "B Type"
        
        elif 20000 > self.income >= 15000:
            self.flat = "C Type"

        else:
            self.flat = "D Type"


    def show_data(self): # Show all the informations
        print("Society Name: ", self.society_name )
        print("Number of Members: ", self.house_no_of_mem)
        print("Income: ", self.income)
        print("Flat: ", self.flat)


ex1 = Society()
ex1.input_data()
ex1.show_data()