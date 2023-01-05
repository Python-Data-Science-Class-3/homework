class ItemInfo():    #define class
    def __init__(self,item_code,price,qty,discount,net_price):
        self.item_code=item_code
        self.price=price
        self.qty=qty    #qty=quantity in stock
        self.discount=discount
        self.net_price=net_price

    def calculate_discount(self):   #calculate discount by a func
        if self.qty<=10:
            return 0.0
        elif 10<self.qty<=20:
            return 0.15
        else:
            return 0.20

    def buy(self):         #input data
        self.item_code=input("Enter item_code :")
        self.price=int(input("Enter price of item:"))
        self.qty=int(input("Enter quantity in stock:"))    
        self.net_price=(self.price)-(self.price*ItemInfo.calculate_discount(self)) #get  calculate func with class name
              
    def show_all(self):    #See details with print func
        print(f'''
-------ItemInfo---------
Item code           :{self.item_code}
Item price          :{self.price}
Quantity in stock   :{self.qty} 
Net Price           :{self.net_price}       ''')          

item_1=ItemInfo('',0,0,0,0)     #create an object
item_2=ItemInfo('',0,0,0,0)

item_1.buy()                    #run func buy 
item_1.show_all()               
item_2.buy()
item_2.show_all()