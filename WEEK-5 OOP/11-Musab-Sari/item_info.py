"""
Developer   : Musab SARI
Date        : 23.01.2023

Question 2: 

Define a class named "Item Info' with the following description: 
item_code (Item Code), item (item name), price (Price of each item), qty (quantity in stock), discount (Discount percentage on the item), net_price (Price after discount) 

Methods:
•	A member method calculate_discount() to calculate discount as per the following rules:
•	If qty <= 10 -> discount is 0
•   If qty (11 to 20 inclusive) -> discount is 15
•	If qty >= 20 -> discount is 20
•	A constructor init method to assign the initial values for item_code to 0 and price, qty , net_price and discount to null
•	A function called buy() to allow user to enter values for item_code, item, price , qty . Then call function calculate_discount() to calculate the discount and net_price (price• qty - discount).
•	A function shoN_all() or similar name to allow user to view the content of all the data members.

"""

class Item_info:
    
    def __init__(self,item_code = 0, item = None, price = None, qty = None, discount = None, net_price = None):
        self.item_code = item_code
        self.item = item
        self.price = price
        self.qty = qty 
        self.discount = discount
        self.net_price = net_price
    
    def calculate_discount(self):
    
        if self.qty <= 10:
            self.discount = 0
    
        elif self.qty >10 and self.qty <= 20:
            self.discount = 15
    
        elif self.qty > 20:
            self.discount = 20
    
        return self.discount
    
    def buy(self):
    
        self.item_code = int(input("Item Code:"))
        self.item = input("Item Name:")
        self.price = float(input("Price of the item:"))
        self.qty = int(input("Quantity:"))
        self.net_price = (self.price*self.qty)*(1-(Item_info.calculate_discount(self))/100)
    
        return self.item_code, self.item, self.price, self.qty, self.net_price
    
    def show_all(self):
    
        print(f"\nItem Code:{self.item_code}\nItem Name:{self.item}\nPrice of the item:{self.price}\nQuantity:{self.qty}\nDiscount rate:%{self.discount}\nNet price of the item:{self.net_price}")

items = Item_info()

newitem = True

while True:
    
    items.buy()
    items.show_all()
    newitem = input("Would you like to add more items to the list?\nPress Y/N: ").upper()
    
    if newitem == "Y":
    
        print("Processing...")
    
    else:
    
        break

