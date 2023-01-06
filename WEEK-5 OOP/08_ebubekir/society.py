'''Question 1:

Create the class society with following information:
society_name , house no_of_mem , flat , income
Methods :
1-	An init method to assign initial values of society_name , house no_of_mem , flat , income
2-	input_date() to read information from members
3-	allocate_flat() to allocate flat according to income using the below table.
4-	show_data() to display the details of the entire class.
Income	Flat
>=25000	A Type
>=20000 and <25000	B Type
>=15000 and <20000	C Type
<15000	D Type
'''

class Society():
    flat=None
    def __init__(self,society_name,house_no_of_mem,flat,income):
        self.society_name=society_name
        self.hausno_of_mem=house_no_of_mem
        self.flat=flat
        self.income=income

    def input_data(self):
        self.society_name=input("Enter society_name :")
        self.hausno_of_mem=input("Enter your house number:")
        self.income=int(input("Enter your income:"))
    
    def allocate_flat(self):
        if self.income>=25000:
            return f'{self.society_name} flat type is : A'
        elif 20000<=self.income<25000:
            return f'{self.society_name} flat type is : B'
        elif 15000<=self.income<20000:
            return f'{self.society_name} flat type is : C'
        else:
            return f'{self.society_name} flat type is : D'   

    def show_data(self):
        print(f"""
    -------Society-------
    Name      :{self.society_name}
    HousNo    :{self.hausno_of_mem}
    Income    :{self.income}
    Flat      :{Society.allocate_flat(self)}"""    )

member1=Society('','','',0)

member1.input_data()           #first take inputs
member1.show_data()            #See datas

        