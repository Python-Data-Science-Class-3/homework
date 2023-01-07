""" 

Developer : Melih Orhan Yilmaz
Date      : 05.01.2023

Application : Customer OOP

Explanation:
Write a Customer class and Items class. Let user enter customer information and add stuff to his/her shopping card.
Class Items : Method: __init__(), __str__(), calculate_discount(), shopping_cart(), get_total_amount() :
total_price = price * qty
discount —> 25% if total_price >= 4000
discount —> 15% if total_price >= 2000
discount —> 10% if total_price < 2000
price_tobe_paid = total_price – discount
shopping_cart():
Let user add items in the shopping basket. Be creative with the items, set their prices as well.
__str__():
Print items added and total price nicely. Class Customer : Methods: __init__()``, get_cust_info()this is optional,str()`
Optionally create a get_cust_info() or similar to allow customer to enter his/her information or just define them in __init__() and pass 
customer information as arguments while creating a customer object.
__str__():
Print customer information and price nicely. Find a way to link two classes. For example, instances of both classes may have a customer number. 
With a get method, get the customer number and pass it to the item object as an argument to set customer number attribute. So Customer class 
instance holds the customer info, Items class holds the shopped item’s info for the same customer ID number such as price, quantity or so.
In the end, print both info (customer info and shopped items info) using their respective __str__ format in a nice way.
Simple example:
Customer1 = [name : Jack, last_name : Russel, customer_id : 123]
shopping_cart1 = [customer_id : 123, items : [necklace, ring, ear ring], total_price : 2000, discount : 300, price_tobe_paid : 1700]
Crate a few customers and print their information (Personal and shopping info).

"""

class Customer():
    number_of_customer = 0

    def __init__(self):
        self.name = input("Name: ")
        self.surname = input("Surname: ")
        Customer.number_of_customer += 1
        self.customer_ID = Customer.number_of_customer

    def __str__(self):
        return f"Name: {self.name}\nSurname: {self.surname}\nCustomer ID: {self.customer_ID}"

class Items(Customer):
    def __init__(self):
        super().__init__()

    items_in_cart = []
    def shopping_cart(self):
        while True:
            self.item_name = input("Item Name: ")
            self.price = int(input("Price of this product: "))
            self.quantity = int(input("How many of this product: "))
            self.cont = input("Enter 'Y' for continue\nEnter 'N' for stop\n")
            if self.cont == "Y" or "y":
                continue
            elif self.cont == "N" or "n":
                break
        
        self.items_in_cart.append(self.item_name)
        self.calculate_discount()
        self.get_total_amount()

        
    def calculate_discount(self, total_price):
        self.total_price = total_price
        self.total_price += self.price
        if self.total_price >= 4000:
            self.discount = 0.25
        elif self.total_price >= 2000:
            self.discount = 0.15
        elif self.total_price < 2000:
            self.discount = 0.10

    def get_total_amount(self):
        self.net_price = self.total_price * (1-self.discount)
        
    def __str__(self):
        return f"Costumer Name : {self.name} Costumer Last Name : {self.surname} Customer ID: {self.customer_ID}\nItems = {self.items_in_cart} Total Price = {self.total_price} Discount: {self.discount} Price Tobe Paid: {self.net_price}"


costumer1 = Items()
costumer1.shopping_cart()
costumer1.calculate_discount()
print(costumer1)

