#Create the class society with following information:
# society_name , house no_of_mem , flat , income
# Methods :
# 1- An init method to assign initial values of society_name , house no_of_mem , flat , income
# 2- input_date() to read information from members
# 3- allocate_flat() to allocate flat according to income using the below table.
# 4- show_data() to display the details of the entire class.
# Income Flat
# >=25000 A Type
# >=20000 and <25000 B Type
# >=15000 and <20000 C Type
# <15000 D Type
#written by Nuseybe 04.01.2023


class Society:
    def __init__(self, society_name , flat, no_of_members,income):
        self.society_name = society_name
        self.income = income
        self.flat = self.allocate_flat()
        self.no_of_members = no_of_members
    
    def allocate_flat(self):                                    #allocating flats by income using the comparison method (from table)
        if self.income >=25000:
            return 'A Type'
        elif 20000<=self.income <25000:
            return 'B Type'
        elif 15000<=self.income <20000:
            return 'C Type'
        else:
            return 'D Type'
    
    def input_data(self):                                        #a method to read information coming  from members 
        while True:
            try:
                self.society_name = input('Enter the Society Name: ')
                self.no_of_members = input('Enter the Number of Members: ')
                self.income = int(input('Enter the Income: '))
                break
            except ValueError:
                print('You entered a wrong value. Please enter a number')
            except :
                print('There was an Error. Please!! Try Again')
        
        self.flat = self.allocate_flat()
    
    def show_data(self):                                            #a method for to display the details of the entire class.
        entry = ''.join (['Society Name: '+self.society_name, '\nFlat Type: '+self.flat, '\nNumber of Members: '+self.no_of_members, '\nIncome : '+str(self.income)])
        return entry

entry_1 = Society(" ", " ", 0, 0)                                   
entry_1.input_data()
print(entry_1.show_data())