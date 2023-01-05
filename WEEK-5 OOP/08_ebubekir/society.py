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

        