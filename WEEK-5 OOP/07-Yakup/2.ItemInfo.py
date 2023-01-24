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
    
    all_data__members=[]
    
   
    def __init__(self,item_code=0, item=None ,price=0.0,qty=0,discount=0,) -> None:
        self.item_code= item_code
        self.item= item
        self.price= price
        self.qty= qty
        self.discount,self.net_price= self.calculate_discount()
        

    

    def  calculate_discount(self):
        
        if (self.qty) <=10:
             self.discount = 0
        
        elif 11<=(self.qty)<=20:
            self.discount = 0.15

        elif (self.qty)>=20:
            self.discount =0.20
        
        self.net_price =(self.price)-(self.price*self.discount)
        return self.discount, self.net_price

    
    
    
    def buy(self):
        self.item_code= input("Enter Item code :")
        self.item= input("Enter Item  :")
        self.price= float(input("Enter price  :"))
        self.qty= int(input("Enter quantity in stock :"))

        
    
    def  add_product(self):  

        ItemInfo.all_data__members.append({'item_code':self.item_code,
                                             'item':self.item,
                                             'price':self.price,
                                             'qty': self.qty,
                                             'net_price':self.net_price
                                             })
        
        print('{} product is added "\n"'.format(ItemInfo.all_data__members))
        
    
    
    def Show_all():
       for item in ItemInfo.all_data__members:
        print (item)



while True:
    print("\n")
    Run_or_stop =input("Please give a command to run the program and enter the product (run R(un), stop S(top) :").upper()
    if Run_or_stop == 'R' :
            new_item = ItemInfo() 
            new_item.buy()
            new_item.calculate_discount()
            new_item.add_product()
            ItemInfo.Show_all()
        
    elif Run_or_stop == 'S':
        print("Thank for use our system..")
        print("\n")
        break
    else:
        print("Please enter one of R or S !")
    
    
        
    


