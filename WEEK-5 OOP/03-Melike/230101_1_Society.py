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

class Society():  ### there should be 'object' in parantheses when we create a class without anything
    data_list = []  ### We don't need to create a list for this process, we have to try to do that without a list.
    def __init__(self, society_name, house_no_of_mem, income, flat="None"):  ### Here should be only "flat", namely without "None" defining
        self.society_name = society_name
        self.house_no_of_mem = house_no_of_mem
        self.income = income
        self.flat = self.allocate_flat()  ### we create first self.flat, her should be only flat when we assign that to self.flat
        
        Society.data_list.append({ "Society Name": self.society_name, "House Number": self.house_no_of_mem, "Income" : self.income, "Flat": self.flat})
        ### This step is not correct. We should do that step for step, but not in this step.
        ### We don't call the class in that class self. After completing of creating the class, 
        ### we can call the required methodes from that class with required objects.

    def input_data():  ### there should be 'self' in parantheses when we create the methode in the class
        a = input("Society Name: ")  ### We have to assign the inputs to the objects we already have created in init function 
        b = input("House Number of Member: ")
        c = int(input("Income: "))
        new_citizen = Society(a, b, c)  ### I have already explained why we can't call the class.
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
            print (i)  ### It would be better if we have used print function to show all attributes without a for loop

deneme1 = Society("MLK", 17, 26000)
deneme2 = Society("XYZ", 5, 17000)
deneme3 = Society("SDK", 7, 23000)

# print(deneme1.allocate_flat())  
# Society.input_data()  ### we should call the methode with the classes which we have already created (deneme1, deneme2, ...)
# Society.show_data()  ### we should call the methode with the classes which we have already created (deneme1, deneme2, ...)

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
