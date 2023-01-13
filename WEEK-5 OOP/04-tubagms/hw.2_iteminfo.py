'''Developer : Tuba GÜMÜS ESMEK
   Date      : 05.01.2023
   Subject   : Iteminfo

'''


'''
Define a class named ``ItemInfo` with the following description:
item_code(Item Code), item(item name), price(Price of each item), qty(quantity in stock), discount(Discount percentage on the item),
net_price(Price after discount)
Methods :
* A member method calculate_discount() to calculate discount as per the following rules:
#If qty <= 10 —> discount is 0
* If qty (11 to 20 inclusive) —> discount is 15
* If qty >= 20 —> discount is 20
* A constructor init method to assign the initial values for item_code to 0 and price, qty, 
net_price and discount to null
* A function called buy() to allow user to enter values for item_code, item, price, qty. 
#Then call function calculate_discount()
 to calculate the discount and net_price(price * qty - discount).
* A function show_all() or similar name to allow user to view the content of all the data members.'''

class Iteminfo:#creating the class Iteminfo
   #creating objects with the init method
   
    
    def __init__(self,item_code, item, price=0, qty=0, discount=0,net_price = 0):
        self.item_code= int(item_code)
        self.item = item
        self.price = float(price)
        self.qty = int(qty)
        self.discount =float(discount)
        self.net_price = float(net_price)


        #getting data from user with buy() method
    def buy(self):
        self.item_code = input("write item code: ")
        self.item = input("write item: ")
        self.price = float(input("write price: "))
        self.qty = int(input("write gty : "))
        self.calculate_discount
        
#using if loop to determine discount wit quantity information with calculate_discount
    def calculate_discount(self):
         
        if self.qty <= 10:
            self.discount = 0
        elif 11<= self.qty <=20:
            self.discount = 0.15
        else:  
            self.discount = 0.20
        self.net_price = self.price * self.qty * (1-self.discount)   
 ##using show_all method to show data members 
    def show_all(self):
       
         return " Iteminfo : {}\n item : {}\n price :{}\n . qty: {}\n net_price :{}". format( self.item_code, self.item, self.price,self.qty, self.net_price)



product1= Iteminfo(0, " ",0,0,0,0)
product1.buy()
print(product1.calculate_discount())

print(product1.show_all())







        

