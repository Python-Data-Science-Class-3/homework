"""
Developer   : Musab SARI
Date        : 23.01.2023

Question 1: 
Create the class Society with the following information:

society_name, house_no_of_mem, flat, income

Methods:

- An __init__ method to assign initial values of society_name, house_no_of_mem, flat, income
- input_data() To read information from members
- allocate_flat() To allocate flat according to income using the below table
- show_data() To display the details of the entire class.

Income               Flat
>=25000              A Type
>=20000 and <25000   B Type
>=15000 and <20000   C Type
<15000               D Type

"""

class Society:

    def __init__(self, society_name = None, house_no_of_mem= None, flat= None, income = None):
        self.society_name = society_name
        self.house_no_of_mem = house_no_of_mem
        self.flat = flat
        self.income = income
    
    def input_data(self):
        self.name = input("Name:")
        self.surname = input("Surname:")
        self.house_no_of_mem = input("House No:")
        self.income = int(input("Income:"))
        self.society_name = self.name + " " + self.surname

    def show_data(self):

        return print(f"Name of member: {self.society_name}\nHouse no of the member: {self.house_no_of_mem}\nFlat Type: {self.flat}\nIncome of the member: {self.income}")
    
    def allocate_flat(self):

        if self.income >= 25000:
            self.flat = "A Type"

        elif self.income >= 20000 and self.income < 25000:
            self.flat = "B Type"

        elif self.income >= 15000 and self.income < 20000:
            self.flat = "C Type"

        elif self.income < 15000:
            self.flat = "D Type"

        return self.society_name, self.house_no_of_mem, self.income, self.flat       

    
society_list = []
a = True

while True:
    
    if a:

        society1 = Society()
        society1.input_data()
        society1.allocate_flat()
        society1.show_data()
        society_list.append(society1.allocate_flat())
        print(society_list)
        userinput = input("Do want to continue to add member into Society?\nIf yes press Y, or press N: ").upper()
    
        if userinput == "Y":

            a = True
        
        else:

            print("Thanks for the contribution!")
            
            a = False

            break