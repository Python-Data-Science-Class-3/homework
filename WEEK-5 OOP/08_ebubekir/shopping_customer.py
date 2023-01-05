'''

Write a Customer class and Items class. Let user enter customer information and add stuff to his/her shopping card. 

Class Items : Method : __init__() ,__str__(), calculate_discount() , shopping_cart() , get_total_amount( )
calculate_discount():
 	total_price = price*qty
 	discount—> 25% if total_price >=4000
 	discount   15% if total_price >=2000
 	discount  10% if total_price < 2000
 	price_tobe_paid = total_price — discount 
shopping_cart():
Let user add items in the shopping basket. Be creative with the items, set their prices as well.
__str__():
•	Print items added and total price nicely. Class Customer : Methods:__init__(), get_cust_info() this is optional, str()'
•	Print items added and total price nicely. Class Customer : Methods: __init__() ,get_cust_info() this is optinal,str()
Optionally create a get_cust_info() or similar to allow customer to enmter his/her information or just define them in __init__() and pass customer information as arguments while creating a customer object.
__str__():
Print customer information and price nicely. Find a way to link two classes. For example, instances of both classes may have a customer number. With a get method, get the customer number and pass it to the item object as an argument to set customer number attribute. So Customer class instance holds thr customer info, Items class holds the shopped item’s info fort he same customer ID number such as price ,quantity or so.
In the end, print both info (customer info and shopped items info) using their respective __str__ format in a nice way.
Simple example:
Customer1 = [name : Jack, last_name : Russel, customer_id : 123] 
Shopping_cart1 =[customer_id : 123, items : [necklace, ring, ear ring], total_price : 2000, discount : 300, price_tobe_paid : 1700 ]
Create a few customers and print their information (Personal and shopping info).

Question 5 (Optional):

Could be a long term project as you may have time. Create a simple game like TicTacToe or similar (Black Jack, paperscissor-rock etc.) using Object Oriented Programming methodology.

'''
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


