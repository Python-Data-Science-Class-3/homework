'''
---PROJECT---
Define a class named ``ItemInfo` with the following description:
item_code(Item Code), item(item name), price(Price of each item), qty(quantity in stock), discount(Discount percentage on the item),
net_price(Price after discount)
Methods :
* A member method calculate_discount() to calculate discount as per the following rules:
* If qty <= 10 —> discount is 0
* If qty (11 to 20 inclusive) —> discount is 15
* If qty >= 20 —> discount is 20
* A constructor init method to assign the initial values for item_code to 0 and price, qty, net_price and discount to null
* A function called buy() to allow user to enter values for item_code, item, price, qty. Then call function calculate_discount()
 to calculate the discount and net_price(price * qty - discount).
* A function show_all() or similar name to allow user to view the content of all the data members.
'''

class iteminfo(): 
    discount = 0 
    def __init__(self,item_code= 0,item =0,price=0,qty=0) : 
        self.item = item 
        self.item_code = item_code 
        self.price = price 
        self.qty = qty 
    def buy(self): 
        self.item_code = input("Item code : ") 
        self.item = input("Item name : ") 
        self.price = int(input("Price : ")) 
        self.qty = int(input("quantity : ")) 
    def calculate_discount(self): 
        if self.qty >= 20: 
            self.discount = 20 
        elif self.qty >= 11: 
            self.discount = 15 
        elif self.qty < 11: 
            self.discount = 0 
    def show_data(self): 
        print("Item Code: ", self.item_code,"\nItem: ", self.item, "\nItem price before discount:", self.price) 
        self.calculate_discount() 
        print("Item price after discount: ", (1-self.discount/100)*self.price) 
item1 = iteminfo() 
item1.buy() 
item1.show_data() 