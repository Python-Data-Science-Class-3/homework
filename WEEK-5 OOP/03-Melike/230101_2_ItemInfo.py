"""
Question 2:

Define a class named "ItemInfo' with the following description: 
item_code (Item Code), item (item name), price (Price of each item), qty (quantity in stock), 
discount (Discount percentage on the item), net_price (Price after discount)

Methods:
- A member method calculate_discount() to calculate discount as per the following rules:
• If qty <= 10 -> discount is 0
• If qty (11 to 20 inclusive) -> discount is 15
• If qty >= 20 -> discount is 20 
- A constructor init method to assign the initial values for item_code to 0 and price, qty, net_price and
discount to null 
- A function called buy() to allow user to enter values for item_code, item, price, qty. Then call function
calculate_discount() to calculate the discount and net_price(price * qty - discount).
• A function show_all() or similar name to allow user to view the content of all the data members."""

class ItemInfo():
    data_list = []
    def __init__(self, item_code=0, item=None, price=None, qty=None, net_price = None, discount = None):
        self.item_code = item_code
        self.item = item
        self.price = price
        self.qty = qty

        self.discount = self.calculate_discount()  ### We must first self.discount create with discount in init function,
        ### every class start with init (initialize) function,
        ### then it can create the other functions with the self objects which has been created with init function. 
        
        self.net_price = int(self.price) - (int(self.price)*int(self.discount)/100)
        ### self.net_price = net_price (this is the correct one)
        ### We will try to use this calculation in the flollowing functions, namely in "calculate_discount" methode.

        ### If you will have to use an object of a function out of that function anywhere in the class,
        ### you will try to create the object in the function with self."object_name" in the class.
        ### But if you won't need to use the variable of a function (namely a local variable), 
        ### you will just create the variable in the function and that variable will live only in that function, 
        ### not in all the class.
        
        ### You are able to call this list using "self.data_list.append...",
        ### you don't need to use the class name. (self = ItemInfo)
        ItemInfo.data_list.append({ "Item Code": self.item_code, "Item Name": self.item, 
        "Price" : self.price, "Quantity in Stock": self.qty, "Discount": self.discount, "Net Price per Item": self.net_price})
    
    def calculate_discount(self):
        if self.qty <= 10:
            self.discount = 0
        elif 10 < self.qty < 20:
            self.discount = 15
        elif self.qty >= 20:
            self.discount = 20
        return self.discount
    
    def buy():
        ### With this function, we try to take the inputs from the user,
        ### and then assign the inputs to our self created attributes, namely global variables in the function.
        a = input("Item Code: ")  ### We will use self.item_code which we have been created in init function, in place of a local variable named "a"
        b = input("Item Name: ")  ### We will use self.item_name here in place of a local variable named "b"
        c = int(input("Price: "))  ### We will use self.price in place of a local variable
        d = int(input("Quantity in Stock: "))  ### We will use self.quantity instead of "d"
        ### Also, they (a, b, c, d) are NOT proper names to name variables. Instead of them, 
        ### it would be better to give the names related to init parameters (item, item_code, ...)
        ### Secondly, it's important to remember to use clearly understandable variable names, NOT a, b, c, d.

        new_item = ItemInfo(a, b, c, d)  
        ### it's not necessary to call the class for this problem
        ### but if you will have to use for another problem,
        ### you can try to apply

        new_item.discount = new_item.calculate_discount()
        new_item.total_net_price = (c - (c * new_item.discount/100)) * d
        print (f"Total price to pay: {new_item.total_net_price}")
    
    def show_all():
        for i in ItemInfo.data_list:  ### 
            print (i)

### why did you take the inputs from the user, if you don't use them?
item1 = ItemInfo("XYZDM12", "tshirt", 100, 12)
item2 = ItemInfo("ABC24", "pants", 100, 22)
item3 = ItemInfo("TYU45", "pull", 250, 8)

# print(item2.net_price)
# ItemInfo.buy()
ItemInfo.show_all()
### You have never used calculate_discount methode, 

### You can take a look at the following solution from me

"""
class ItemInfo:

    def __init__(self, item_code = 0, item = None, price = 0, qty = 0, discount = 0, net_price = 0):
        self.item_code = item_code
        self.item = item
        self.price = price
        self.qty = qty
        self.discount = discount
        self.net_price = net_price

    def calculate_discount(self):
        if self.qty <= 10:
            self.discount = 0

        elif 11 <= self.qty < 20:
            self.discount = 15

        elif self.qty >= 20:
            self.discount = 20

        self.net_price = self.price * self.qty - self.discount

    def buy(self):
        self.item_code = input("Type the code of the item: ")
        self.item = input("Type the name of the item: ")
        self.price = int(input("Type the price of the item: "))
        self.qty = int(input("Type the quantity of the item: "))

        self.calculate_discount()

    def show_all(self):
        return {
                "item_code":self.item_code, 
                "item_name":self.item, 
                "item_price":self.price, 
                "item_quantity":self.qty, 
                "discount_amount":self.discount, 
                "net_price":self.net_price
                }


all_items = []  # for creating a list to show all items which will have been created with inputs

finished = False

while not finished:  

    item = ItemInfo()
    item.buy()
    print(item.show_all())
    all_items.append(item.show_all())

    inp = input("Will you want to add new item, then you can go ahead with typing any button then Enter. \nIf you want to stop, you can type just 'N'")

    if inp == "N":
        finished = True

print(all_items)

"""
