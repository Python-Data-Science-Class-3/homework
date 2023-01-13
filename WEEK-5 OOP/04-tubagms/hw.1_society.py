'''Developer : Tuba GÜMÜS ESMEK
   Date      : 05.01.2023
   Subject   : Society

'''

'''
Create the class Society with following information:
society_name,house_no_of_mem, flat, income
Methods :
- An __init__ method to assign initial values of society_name,house_no_of_mem, flat, income
- input_data() To read information from members
- allocate_flat() To allocate flat according to income using the below table.
- show_data() to display the details of the entire class.
Income	            Flat
>=25000	            A Type
>=20000 and <25000	B Type
>=15000 and <20000	C Type
<15000	            D Type'''

class Society:  #creating the  class Society
    #creating objects with the init method
    
    def __init__(self, society_name, house_no_of_nem, income, flat = " "):
        self.society_name = society_name
        self.house_no_of_nem = house_no_of_nem
        self.flat =str(flat)
        self.income = int(income)

    def input_data(self):              #getting data from user with input_data method
        self.society_name = input("write your society-name : ")
        self.house_no_of_nem = input("Write your house no: ")
        #self.flat = input("write your flat: ")
        self.income= int(input("write your income: "))
        self.allcoate_flat()

#determine flat by income using an if loop
    def allcoate_flat(self):
        if self.income >=250000:
           return  " A Type"
        elif 20000  <= self.income < 25000 :
            return "B Type"
        elif 15000 <= self.income < 20000:
            return  "C Type"
        else:
            return "D Type"
#using show_data method to show all information
    def show_data(self):
       return "society_name : {}\n house_no_of_nem : {}\n income : {}\n self.flat : {}". format(self.society_name, self.house_no_of_nem, self.income, self.allcoate_flat())
       
        

society1 = Society(" ", " ",0," ")
society1.input_data()
society1.allcoate_flat
print(society1.show_data())








    
    
