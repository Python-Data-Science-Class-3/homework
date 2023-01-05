"""
Author: Adem DOĞAN

Create the class society with following information:
society_name , house no_of_mem , flat , income
Methods :
1-	An init method to assign initial values of society_name , house no_of_mem , flat , income
2-	input_date() to read information from members
3-	allocate_flat() to allocate flat according to income using the below table.
4-	show_data() to display the details of the entire class.

Date :1/2023
"""

class Society:

    def __init__(self,society_name, house_no_of_mem, flat,income):
        self.society_name = society_name
        self.house_no_of_mem = house_no_of_mem
        self.flat = flat
        self.income = income
    
    #Get data from user
    def input_data(self):
        self.society_name = input(" Enter society name")
        self.house_no_of_mem =int(input("Enter number of member in the house")) 
        self.income = float(input("Enter income"))
      
    #Determination of the appropriate type according to income
    def allocate_flat(self):
        if self.income >= 25000:
            self.flat = "A type of flat"
        elif self.income >=20000 and self.income<25000:
             self.flat = "B type of flat"
        elif self.income >=15000 and self.income<20000:
             self.flat = "C type of flat"
        elif self.income <15000:
             self.flat = "D type of flat"

    #Display of results on screen
    def show_data(self):
        print(f"Society name = {self.society_name}")
        print(f"House number = {self.house_no_of_mem}")
        print(f"House type = {self.flat}")
        print(f"Income = {self.income}")
    

society = Society("", 0, "", 0)
society.input_data()
society.allocate_flat()
society.show_data()