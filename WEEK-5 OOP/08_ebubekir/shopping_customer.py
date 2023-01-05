class Items():     #create an item class
    def __init__(self,item_id,item_name,qty,price,total_price,price_tobe_paid): 
        self.item_id=item_id
        self.item_name=item_name
        self.qty=qty
        self.price=price
        self.total_price=total_price
        self.price_tobe_paid=price_tobe_paid

    def shopping_card(self):             #define a func to get input
        self.item_name=input("Enter item name:")
        self.qty=int(input("Enter quantity of the item:"))
        self.price=int(input("Enter price of the item:"))

    def __str__(self):      #See the shopping details with print func
        print(f'''
-------Shopping Details----
Item name        :{self.item_name}
Quantity of item :{self.qty}
Price            :{self.price}
Discount         :{Items.calculate_discount(self):.5}
Price to be paid :{Items.get_total_amount(self)} ''')

    

    def calculate_discount(self):              #define a func to calculate discount
        self.total_price=self.price*self.qty
        if self.total_price>=4000:
            return self.total_price*0.25
        elif 4000 > self.total_price>=2000:
            return self.total_price*0.15 
        elif self.total_price<2000:
            return 2000 > self.total_price*0.10

    def get_total_amount(self):              #define a func to find total amount
        self.price_tobe_paid=self.total_price-Items.calculate_discount(self)  
        return self.price_tobe_paid
        
class Customer():  #create a customer class
    def __init__(self,customer_name,customer_last_name,customer_id):
        self.customer_name = customer_name
        self.customer_lastname = customer_last_name
        self.customer_id = customer_id
    
    def get_customer_data(self):     #define a func to get input
        self.customer_name=input("Enter your name? ")
        self.customer_lastname=input("Enter your lastname? ")
        self.customer_id=int(input("Enter your customer ID? "))

    def __str__(self):               #see details with __str__
        print(f'''
-------Customer Datas--------
Customer name    :{self.customer_name}
Customer lastname:{self.customer_lastname}
Customer id      :{self.customer_id}        ''')

customer1=Customer('','',0)             #create an object in customer class
customer1.get_customer_data()           #Take data inputs  by func 

item_1=Items(0,'',0,0,0,0)              #create an object in Items class
item_1.shopping_card()

customer1.__str__()                    #see details 
item_1.__str__()


