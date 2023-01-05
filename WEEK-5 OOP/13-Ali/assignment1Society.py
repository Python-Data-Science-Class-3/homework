'''Create the class society with following information:
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

import json
class Society:
    members = {}
    memNum = 0
    def __init__(self, society_name="",house_no_of_mem="",flat="",income=int()):
        Society.memNum += 1
        self.memberNum = "member"+str(Society.memNum)        
        self.society_name = society_name
        self.house_no_of_mem = house_no_of_mem
        self.flat = flat
        self.income =income
        self.input_data()
        self.allocate_flat()
        self.addMember()
        Society.show_data()
        # Society.memNum += 1     # bu iki satırı init funk başına aldık yoksa ilk elemanda 0 veriyor sanradan hesaplayınca!
        # self.memberNum = Society.memNum    

    def input_data(self):
        self.society_name = input("enter name and surname with a blank between them:")
        self.house_no_of_mem = int(input("enter  house number: "))
        self.income = int(input("enter your income: "))
        return self.society_name
        return self.house_no_of_mem
        return self.income

    def allocate_flat(self):   # in this step flats are being allocated
        if self.income < 15000:
            self.flat = "D type"
        elif 15000 <= self.income < 20000:
            self.flat = "C type"  
        elif 20000 <= self.income < 25000:
            self.flat = "B type"  
        else:
            self.flat = "A type"  
        return self.flat
    def addMember(self):
        Society.members[self.memberNum]={"society_name": self.society_name, "house_no_of_member": self.house_no_of_mem,"flat":self.flat, "income":self.income}

    @classmethod
    def show_data(cls):
        print(json.dumps(Society.members, indent=4))
     
            
associated = []  #from this step assignment of objects is automaticated 
while True:   #this iteration works in case that user enters information via input above
    newAssociated = Society()  
    newAssociated.input_data
    associated.append(newAssociated)
 


