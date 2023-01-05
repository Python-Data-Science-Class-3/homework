"""
Question 1
Create the class Society with following information: society_name, house_no_of_mem, flat, income

Methods:
• An _init_ method to assign initial values of society_name, house_no_of_mem, flat, income
• input_data() To read information from members
• allocate_flat() To allocate flat according to income using the below table.
• show data() to display the details of the entire class.
> =25000                A Type
> =20000 and <25000     B Type
>=15000 and <20000      C Type
<15000                  D Type"""

class Society():
    data_list = []
    def __init__(self, society_name, house_no_of_mem, income, flat="None"):
        self.society_name = society_name
        self.house_no_of_mem = house_no_of_mem
        self.income = income
        self.flat = self.allocate_flat()
        
        Society.data_list.append({ "Society Name": self.society_name, "House Number": self.house_no_of_mem, "Income" : self.income, "Flat": self.flat})

    def input_data():
        a = input("Society Name: ")
        b = input("House Number of Member: ")
        c = int(input("Income: "))
        new_citizen = Society(a, b, c)
        return new_citizen
        
    
    def allocate_flat(self):
        if self.income >= 25000:
            self.flat = "A Type"
        elif 25000 > self.income >= 20000:
            self.flat = "B Type"
        elif 20000 > self.income >= 15000:
            self.flat = "C Type"
        elif self.income < 15000:
            self.flat = "D Type"
        return self.flat

    
    def show_data():
        for i in Society.data_list:
            print (i)

deneme1 = Society("MLK", 17, 26000)
deneme2 = Society("XYZ", 5, 17000)
deneme3 = Society("SDK", 7, 23000)

# print(deneme1.allocate_flat())
# Society.input_data()
Society.show_data()
