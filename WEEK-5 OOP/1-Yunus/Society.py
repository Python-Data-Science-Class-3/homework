'''
---PROJECT---
Create the class Society with following information:
society_name,house_no_of_mem, flat, income
Methods :
- An __init__ method to assign initial values of society_name,house_no_of_mem, flat, income
- input_data() To read information from members
- allocate_flat() To allocate flat according to income using the below table.
- show_data() to display the details of the entire class.
Income	Flat
>=25000	A Type
>=20000 and <25000	B Type
>=15000 and <20000	C Type
<15000	D Type
'''


class Society:
    informaton = []
    def __init__(self,society_name,house_no_of_mem,income,flat = "") :
        self.society_name = society_name
        self.house_no_of_mem = house_no_of_mem
        self.flat=flat
        self.income = income
    def input_data(self):
        self.society_name = input("enter the society name : ")  
        self.house_no_of_mem = input("house no  : ")
        # self.flat= input("flat type : ")
        self.income= int(input("enter income : "))

    def allocate_flat(self):
        if self.income >= 25000 :
            self.flat = "A"
        elif self.income >= 20000 :
            self.flat = "B"
        elif self.income >= 15000 :
            self.flat = "C"
        elif self.income < 25000 :
            self.flat = "D"
    def show_data(self):
        print(f"{self.society_name} can have {self.flat} type house...")
        print(f"has {self.house_no_of_mem} houses and  {self.income} as income ")
        
mem1 = Society

    
Society.input_data(mem1)
Society.allocate_flat(mem1)
Society.show_data(mem1)
