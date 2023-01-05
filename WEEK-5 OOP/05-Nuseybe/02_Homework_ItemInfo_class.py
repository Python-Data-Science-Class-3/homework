#Define a class named Itemlnfa' with the following description;
# item_code   (Item   Code),   item   (item   name),   price   (Price   of   each   item),   qty  (quantity  in   stock),   
# discount   (Discount percentage on the item), net_price (P rice after discount)
# Methods :
# •A member method calculate_discount() to calculate discount as per the following rules:
# • If qty <=10--->discount is 10
# •If qty (11 to 28 inclusive)---> discount is 15
# •If qty  >=20 -- discount is 20
# •A constructor init method to assign the initial values for item_code to 0 and price , qty , net_price and discount to null
# •A   function   called   buy()   to   allow   user   to   enter   values   for   item_code   ,   item,   price   ,   qty   .   Then   call   function
# calculate_discount() to calculate the discount and net_price (price*qty - discount).
# •A function show_all() or similar name to allow user to view the content of all the data members
#Written buy Nuseybe at 05.01.2023



class ItemInfo():
    def __init__(self, item_code = 0, item_name = " ", price = " ", qty = " ", discount = " ", net_price = " "):
        self.item_code = item_code
        self.item = item_name 
        self.price = price 
        self. qty = qty
        self. discount = discount 
        self.net_price= net_price
    
    def buy(self):                                                                  #a method  for to   allow   user   to   enter   values
        try : 
            self.item_code = input("Please enter a code for item:  ")                   
            self.item = input("Please enter item's name:  ")
            self.price = int(input("Please enter the price of item:  "))
            self.qty = int(input("Please enter the quantity of item:  "))
            self.discount = self.calculate_discount()                                       #calling the method of discount calculate
            self.net_price = self.price * self.qty - ItemInfo.calculate_discount(self)      #calculation of the discount and total discounted price according to the number of products in stock 
        
        except ValueError:
            print("Please enter a number ")                                                 #Value error chcek
            return self.buy()

    def calculate_discount(self):                                                           #the method that provides the calculation of the discount according to the number of products in stock
        if self.qty <=10 :
            return 0
        elif self.qty >=11 and self.qty <20 :
            return 15
        else : 
            return 20

    def show_all(self):                                                                     #the method for view the content of all the data members
        return (f"""
        Item's Code     : {self.item_code}
        Item's  Name    : {self.item}
        Item's Price    : {self.price}
        Item's Quantity : {self.qty}
        Discount %      : {self.discount}
        Rercent of Discount Price : {self.net_price}

        """)

new_entry = ItemInfo()
new_entry.buy()
print(new_entry.show_all())

        
