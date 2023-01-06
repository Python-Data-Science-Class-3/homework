'''Developer : Tuba GÜMÜS ESMEK
   Date      : 05.01.2023
   Subject   : Society

'''
#Create the class Society with following information:
#society_name,house_no_of_mem, flat, income
#Methods :
#- An __init__ method to assign initial values of society_name,house_no_of_mem, flat, income
#- input_data() To read information from members
#- allocate_flat() To allocate flat according to income using the below table.
#- show_data() to display the details of the entire class.
#Income	            Flat
#>=25000	            A Type
#>=20000 and <25000	B Type
#>=15000 and <20000	C Type
#<15000	            D Type

class Society:  #creating the  class Society
    #creating objects with the init method
    def __init__(self, society_name= None, house_no_of_nem= None, flat= " ", income=0):
        self.society_name = society_name
        self.house_no_of_nem = house_no_of_nem
        self.flat = str(flat)
        self.income = int(income)

    def input_data(self):           #getting data from user with input_data method
        self.society_name = input("write your society-name : ")
        self.house_no_of_nem = input("Write your house no: ")
        #self.flat = input("write your flat: ")
        self.income= input("write your income: ")

    #determine flat by income using an if loop
    def allcoate_flat(self):        
        if self.income >=250000:
           self.flat = " A Type"
        elif 20000  <= self.income < 25000 :
            self.flat = "B Type"
        elif 15000 <= self.income < 20000:
            self.flat = "C Type"
        else:
            self.flat = "D Type"
    #using show_data method to show all information
    def show_data(self):
       return "society_name : {}\n house_no_of_nem : {}\n income : {}\n flat : {}". format(self.society_name, self.house_no_of_nem, self.income, self.flat)
        #return f'Society({self.society_name},{self.house_no_of_nem},{self.flat},{self.income})'
        

society1 = Society()
society1.input_data()
society1.allcoate_flat
print(society1.show_data())
