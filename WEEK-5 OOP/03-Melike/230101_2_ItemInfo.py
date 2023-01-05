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

        self.discount = self.calculate_discount()
        self.net_price = int(self.price) - (int(self.price)*int(self.discount)/100)

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
        a = input("Item Code: ")
        b = input("Item Name: ")
        c = int(input("Price: "))
        d = int(input("Quantity in Stock: "))
        new_item = ItemInfo(a, b, c, d)

        new_item.discount = new_item.calculate_discount()
        new_item.total_net_price = (c - (c * new_item.discount/100)) * d
        print (f"Total price to pay: {new_item.total_net_price}")
    
    def show_all():
        for i in ItemInfo.data_list:
            print (i)


item1 = ItemInfo("XYZDM12", "tshirt", 100, 12)
item2 = ItemInfo("ABC24", "pants", 100, 22)
item3 = ItemInfo("TYU45", "pull", 250, 8)

# print(item2.net_price)
# ItemInfo.buy()
ItemInfo.show_all()
