#Write a Customer class and Items class. Let user enter customer information and add stuff to his/her shopping card.
# Class Items :
# Method : __init__(), __str__(), calculate_discount(), shopping_cart(), get_total_amount()
# calculate_discount():
# total_price = price * qty
# discount —> 25% if total_price >= 4000
# discount —> 15% if total_price >= 2000
# discount —> 10% if total_price < 2000
# price_tobe_paid = total_price – discount
# shopping_cart():
# Let user add items in the shopping basket. Be creative with the items, set their prices as well.__str__():
# Print items added and total price nicely.
# Class Customer :
# Methods: __init__(), get_cust_info() this is optional, __str__()
# Optionally create a get_cust_info() or similar to allow customer to enter his/her information or just define them in __init__()
# and pass customer information as arguments while creating a customer object.__str__():
# Print customer information and price nicely.
# Find a way to link two classes. For example, instances of both classes may have a customer number. With a get method,
#  get the customer number and pass it to the item object as an argument to set customer number attribute. So Customer class instance holds the customer info, 
# Items class holds the shopped item’s info for the same customer ID number such as price, quantity or so.
# In the end, print both info (customer info and shopped items info) using their respective __str__ format in a nice way.
# Simple example:
# Customer1 = [name : Jack, last_name : Russel, customer_id : 123]
# shopping_cart1 = [customer_id : 123, items : [necklace, ring, ear ring], total_price : 2000, discount : 300,  price_tobe_paid : 1700]
# Crate a few customers and print their information (Personal and shopping info).
#Written by Nuseybe at 05.01.2023

class Customer:                                                                 # A Class for Customer value
    def __init__(self, name, surname, cust_id ):                  
        self.name = name
        self.surname = surname
        self.cust_id = cust_id
      

    def get_customer_info(self):                                                #a method to enter value 
        self.name = input("Please enter the customer name :  ")
        self.surname = input("Please enter the customer surname :  ")
       
      

    def __str__ (self):
        return (f"""
        Customer Name    : {self.name}
        Customer Surname : {self.surname}
        Customer ID      : {self.cust_id}
        """)
   
class Item:
    def __init__(self, product_name="", product_qty=0, product_price=0, total_price=0 , discount=0 , cust_id=0):
        self. product_name = product_name
        self.product_qty = product_qty
        self.product_price = product_price
        self.total_price = total_price
        self.discount = discount
        self.cust_id = cust_id

    def __str__ (self):
        self.shopping_cart = []
        return (f"""
        Customer ID        : {self.cust_id}
        Product Name       : {self.product_name}
        Number of Product  : {self.product_qty}
        Product Price      : {self.product_price}
        Discount           : {self.discount}
        Total Payment      : {self.total_pay}
       
        """)

    def get_total_payment(self):
        self.total_pay= self.total_price - self.discount
        return self.total_pay

    def calculate_discount(self):
        self.total_price = self.product_price * self.product_qty
        if self.total_price < 2000 :
            self.discount = self.total_price * 0.1
        elif self.total_price <= 4000 :
            self.discount = self.total_price * 0.15
        elif self.total_price > 4000 :
            self.discount = self.total_price * 0.25

    def shopping_cart(self,x):
        try:
            self.product_name = str(input("Please enter the Product Name:  "))
            self.product_qty = int ( input(" Please enter the Number of Product:  "))
            self.product_price = int(input(" Please enter Product Price:  "))
            self.calculate_discount()
            self.get_total_payment()


        except ValueError():
            print("Please check the entry value ")
            return self.shopping_cart()

new_customer = Customer(" "," ",0)
new_customer.get_customer_info()

new_product = Item()
new_product.shopping_cart(new_customer.cust_id)

print(new_customer)
print(new_product)
