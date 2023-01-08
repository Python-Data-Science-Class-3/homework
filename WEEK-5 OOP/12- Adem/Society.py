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
    ### It would be better if you have assigned "None" values to the attributes,
    ### otherwise you must use an initial values for all objests
    ### if you assign 'None' to all attributes, you won't have to define the initial values for them 
    ### when you create the class
    ### as you already have made (society = Society("", 0, "", 0))   

        self.society_name = society_name
        self.house_no_of_mem = house_no_of_mem
        self.flat = flat
        self.income = income
    
    #Get data from user
    def input_data(self):  ### well done
        self.society_name = input(" Enter society name")
        self.house_no_of_mem =int(input("Enter number of member in the house"))
        self.income = float(input("Enter income"))
      
    # Determination of the appropriate type according to income
    def allocate_flat(self):  ### well done
        if self.income >= 25000:
            self.flat = "A type of flat"
        elif self.income >=20000 and self.income<25000:
             self.flat = "B type of flat"
        elif self.income >=15000 and self.income<20000: 
             self.flat = "C type of flat"
        elif self.income <15000:
             self.flat = "D type of flat"

    # Display of results on screen
    def show_data(self):
        print(f"Society name = {self.society_name}")
        print(f"House number = {self.house_no_of_mem}")
        print(f"House type = {self.flat}")
        print(f"Income = {self.income}")
    

society = Society("", 0, "", 0)  ### I have already tried to explain why you were not able to use it without initial values
society.input_data()
society.allocate_flat()
society.show_data()

### I've attached a solution from me below, if you want to take a look

"""
class Society(object):
    
    def __init__(self, society_name = None, house_no_of_mem = None, flat = None, income = None):
        # initializing values
        self.society_name = society_name
        self.house_no_of_mem = house_no_of_mem
        self.flat = flat
        self.income = income

    def input_data(self):
        # taking the inputs from the members
        self.society_name = input('You will please write your society name: ')
        self.house_no_of_mem = input('You will please write your house number: ')
        self.income = int(input('You will please write your annual income: '))
        
        
    def allocate_flat(self):
        # defining the flat type
        if self.income >= 25000:
            self.flat = "A Type"
        elif 25000 > self.income >= 20000:
            self.flat = "B Type"
        elif 20000 > self.income >= 15000:
            self.flat = "C Type"
        elif self.income < 15000:
            self.flat = "D Type"

        return self.society_name, self.house_no_of_mem, self.income, self.flat
        
        # return self.flat
    
    def show_data(self):
        
        print(f"\nSociety name : {self.society_name}\nHouse no : {self.house_no_of_mem}",
              f"\nIncome of member : {self.income}\nFlat Type to member : {self.flat}\n")
        

members = []  # for creating a list to show all members which will have been created with inputs

finished = False

while not finished:  

    member = Society()
    member.input_data()
    # member.allocate_flat()
    members.append(member.allocate_flat())

    member.show_data()

    inp = input("Will you want to add new information, then you can go ahead with typing any button then Enter. \nIf you want to stop, you can type just 'N'")

    if inp == "N":
        finished = True

print(members)
"""