# Create the class Society with following information:
# society_name,house_no_of_mem, flat, income
# Methods :
# An __init__ method to assign initial values of society_name,house_no_of_mem, flat, income
# input_data() To read information from members
# allocate_flat() To allocate flat according to income using the below table.
# show_data() to display the details of the entire class.
# Income	            Flat
# >=25000	            A Type
# >=20000 and <25000	B Type
# >=15000 and <20000	C Type
# <15000	            D Type



class Society:
    def __init__(self,society_name = '',house_no_of_mem = 0,flat = None,income = 0):
        self.society_name = society_name
        self.house_no_of_mem = house_no_of_mem
        self.income = income
        self.flat = flat

    def input_data(self):
        self.society_name = input("Enter your society name:")
        self.house_no_of_mem = int(input("Enter your house number:"))
        self.income = int(input("Enter your income:"))
        self.flat = input("Enter your flat type:")

    def allocate_flat(self):
        if self.income >= 25000:
           return "Type A" 

        elif 20000 >= self.income > 25000:
           return "Type B"

        elif 15000 >= self.income >20000:
           return "Type C"

        else:
            return "Type D"


    def show_data(self):
        print(f"\nSociety name : {self.society_name}\nHouse no : {self.house_no_of_mem}",
              f"\nIncome of member : {self.income}\nFlat Type to member : {self.flat}\n") 


society1 = Society()
society1.input_data()
society1.show_data()