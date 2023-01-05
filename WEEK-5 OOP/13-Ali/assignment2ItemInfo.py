'''Define a class named Itemlnfa' with the following description;
item_code (Item Code), item (item name), price (Price of each item), qty (quantity in stock), discount (Discount percentage on the item), net_price (P rice after discount)
Methods :
•	A member method calculate_discount() to calculate discount as per the following rules:
•	 If qty <=10--->discount is 10
•	If qty (11 to 28 inclusive)	---> discount is 15
•	If qty  >=20 -- discount is 20
•	A constructor init method to assign the initial values for item_code to 0
    and price , qty , net_price and discount to null
•	A function called buy() to allow user to enter values for item_code , item, price , qty .
    Then call function calculate_discount() to calculate the discount and net_price (price*qty - discount).
•	A function show_all() or similar name to allow user to view the content of all the data members.
'''


import json
class ItemInfo:
    storage = {}
    def __init__(self,item_code =0, item= "", price = int(), qty = int(),\
discount = int(), net_price= int()):
        self.item_code = item_code
        self.item = item
        self.price = price
        self.qty = qty
        self.discount = discount
        self.net_price = net_price
        self.buy()
        self.calculate_discount()
        self.add_member()
        self.show_all()
        
        
    def calculate_discount(self):   # in this step discount is being calculated
        if self.qty <= 10:
            self.discount = 0
        elif 10 < self.qty < 20:
            self.discount = 15
        else:
            self.discount = 20
        self.net_price = self.price*(1-(self.discount)*0.01)
            
        return (self.discount, self.net_price)
    def buy(self):
        self.item_code = int(input("enter itme code in digits to add new item: "))
        self.item = input("enter itme name to add new item: ")
        self.price = int(input("enter price of new item: "))
        self.qty = int(input("enter quantity of new item in stock: "))
    def add_member(self):
        ItemInfo.storage["item code: " + str(self.item_code)] = {"item name":self.item, "price of item":self.price,\
"quantity in stock":self.qty,"discount percentage on the item":self.discount,"price after discoun":self.net_price}
    @classmethod
    def show_all(cls):   # in this step the new being informations given by the method buy is being added the class repository "storage"
        print(json.dumps(ItemInfo.storage, indent=4))
entities = []

while True:        #from this step assignment of objects is automaticated 
    newEntity = ItemInfo()     #this iteration works in case that user enters information via input above
    newEntity.buy
    entities.append(newEntity)
        
        
