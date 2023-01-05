""" 

Developer : Melih Orhan Yilmaz
Date      : 05.01.2023

Application : ItemInfo OOP

Explanation : 
Define a class named ``ItemInfo` with the following description:
item_code(Item Code), item(item name), price(Price of each item), qty(quantity in stock)discount(Discount percentage on the item), net_price(Price after discount)
Methods :
A member method calculate_discount() to calculate discount as per the following rules:
If qty <= 10 —> discount is 0
If qty (11 to 20 inclusive) —> discount is 15
If qty >= 20 —> discount is 20
A constructor init method to assign the initial values for item_code to 0 and price, qty, net_price and discount to null
A function called buy() to allow user to enter values for item_code, item, price, qty. 
Then call function calculate_discount() to calculate the discount and net_price(price * qty - discount).
A function show_all() or similar name to allow user to view the content of all the data members.

"""

class ItemInfo():

    def __init__(self, item_code = 0, item = "", price = 0, qty = 0, discount=0, net_price=0):
        self.item_code = item_code
        self.item = item
        self.price = price
        self.qty = qty
        self.discount = discount
        self.net_price = net_price

    def buy(self):
        
        self.item_code = int(input("Enter Item Code: ")) 
        self.item=input("Enter Item Name: ") 
        self.price = float(input("Enter Item Price: "))
        self.qty = int(input("Enter Quantity of Item: ")) 
        self.calculate_discount() # Call calculate_discount
        self.net_price_final() # Call net_price_final

        return self.item_code, self.item, self.price, self.qty

    def calculate_discount(self):
        if self.qty <= 10:
            self.discount = 0.0
        elif 10 < self.qty < 20:
            self.discount = 0.15
        else:
            self.discount = 0.20
    
    def net_price_final(self):
        self.net_price = self.price * self.qty * (1-self.discount)

    def show_all(self):
        print(f"""

---------Item Info---------
Item Code: {self.item_code}
Item: {self.item}
Price: {self.price}
Quantity: {self.qty}
Discount: {self.discount}
Net Price: {self.net_price}

""")

i = ItemInfo()
i.buy()
i.show_all()