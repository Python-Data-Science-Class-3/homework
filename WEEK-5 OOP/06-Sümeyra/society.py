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
    def __init__(self,society_name = '',house_no_of_mem = 0,flat = None,income = 0):  ### We could use None for all
        self.society_name = society_name
        self.house_no_of_mem = house_no_of_mem
        self.income = income
        self.flat = flat

    def input_data(self):
        self.society_name = input("Enter your society name:")
        self.house_no_of_mem = int(input("Enter your house number:"))
        self.income = int(input("Enter your income:"))
        self.flat = input("Enter your flat type:") ### Type of flat should be determined using the class, no with the user input.
        ### We have to allocate the type of flat with the following 'allocate_flat' function

    def allocate_flat(self):   
    ### We should assign the type of the flat to the self.flat object for every condition,
    ### then we can use return if we need that.
    ### If we don't call this methode after creation of the class, we won't be able to allocate the correct flat type
    
        if self.income >= 25000:
           return "Type A" 

        elif 20000 >= self.income > 25000:  ### This condition is not true
           return "Type B"

        elif 15000 >= self.income >20000:  ### This condition is also not true
           return "Type C"

        else:
            return "Type D"


    def show_data(self):
        print(f"\nSociety name : {self.society_name}\nHouse no : {self.house_no_of_mem}",
              f"\nIncome of member : {self.income}\nFlat Type to member : {self.flat}\n") 


society1 = Society()
society1.input_data()
society1.allocate_flat()
society1.show_data()
### 'allocate_flat' methode should be called before it the show_data methode

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
