"""
Author: Adem DOĞAN

Define a class named Itemlnfa' with the following description;
item_code (Item Code), item (item name), price (Price of each item), qty (quantity in stock), discount
(Discount percentage on the item), net_price (P rice after discount)
Methods :
•	A member method calculate_discount() to calculate discount as per the following rules:
•	 If qty <=10--->discount is 10
•	If qty (11 to 28 inclusive)	---> discount is 15
•	If qty  >=20 -- discount is 20
•	A constructor init method to assign the initial values for item_code to 0 and price , qty , net_price 
and discount to null
•	A function called buy() to allow user to enter values for item_code , item, price , qty .
Then call function calculate_discount() to calculate the discount and net_price (price*qty - discount).
•	A function show_all() or similar name to allow user to view the content of all the data members.

Date :1/2023
"""
class Iteminfo:

    def __init__(self):
        self.item_code = 0
        self.item = None
        self.price = None
        self.qty =  None
        self.discount = None
        self.net_price = None

    #Finding a discount that varies by quantity
    def calculate_discount(self):
        if self.qty <= 10:
            self.discount = 10

        if self.qty >= 11 or self.qty<=28 :
            self.discount = 15

        if self.qty >=20:
            self.discount =20

    #Entering information and calculating the price
    def buy(self,item_code,item,price,qty):
        self.item_code = item_code
        self.item = item
        self.price = price
        self.qty = qty
        self.calculate_discount()
        self.net_price = self.price*self.qty -self.discount
        
    #Show all content
    def show_all(self):
        print(f"Item code:", self.item_code)
        print(f"Item :", self.item)
        print(f"Price :", self.price)
        print(f"Quantity :", self.qty)
        print(f"Discount :", self.discount)
        print(f"Net Price :", self.net_price)

item = Iteminfo()
#Calling the function by entering the values of item_code,item,price,qty
item.buy(12, "Iphone 13", 20, 15)
item.show_all()