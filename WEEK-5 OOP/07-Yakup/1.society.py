'''Create the class society with following information:
society_name , house no_of_mem , flat , income
Methods :
1-	An init method to assign initial values of society_name , house no_of_mem , flat , income
2-	input_date() to read information from members
3-	allocate_flat() to allocate flat according to income using the below table.
4-	show_data() to display the details of the entire class.

Income	                Flat

>=25000	                A Type
>=20000 and <25000	    B Type
>=15000 and <20000	    C Type
<15000	                D Type
'''

class Community():

    community_list= []
    house_no = 0
    


    def __init__(self,society_name =None, flat=None , income=None) -> None:
       
       Community.house_no +=1
       self.society_name = society_name
       self.house_no_of_member= Community.house_no
       self.flat=flat
       self.income= income
       Community.community_list.append([
                        self.society_name,
                        self.house_no_of_member,
                        self.flat,
                        self.income
                        ])

    def input_date(self):
        self.society_name = input('Enter your society nane : ')
        self.income= input("Enter your income :")
        self.allocate_flat()
          
    
    
    def allocate_flat(self):
        if (int(self.income)) >= 25000:
            self.flat = "A Type"
        elif  20000 <= (int(self.income)) <= 25000:
            self.flat = "B Type"
        elif  15000 <= (int(self.income)) <= 20000:
            self.flat = "CType"
        elif   (int(self.income)) <= 15000:
            self.flat = "D Type"
            


    @classmethod
    def Showdata(cls):
        print("\n")
        print("The details of the Community")
        print("_"*100)
        print([*map(lambda x: x,cls.community_list )])
        print("_"*100)

while True:
    val = input("Do you want to register? Y(es)/N(o)").upper()
    if val == "Y" :
        menber=Community()
        menber.input_date()
        

        
    else:
        Community.Showdata()
        break