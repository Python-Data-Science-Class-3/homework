"""
Question 4:
Write a Customer class and Items class. Let user enter customer information and add stuff to his/her shopping card.

Class Items: Method:_init__(), __str__(), calculate_discount(), shopping_cart(), get_total_amount()

calculate_discount:
• total_price = price * qty
• discount -> 25% if total_price >= 4000
• discount -> 15% if total price >= 2000
• discount -> 10% if total price < 2000
• price_to_be_paid = total price - discount

shopping_cart:
Let user add items in the shopping basket. Be creative with the items, set their prices as well.

__str__():
• Print items added and total price nicely. 

Class Customer: Methods: __init__(), get_cust_info() this is optional, str()

Optionally create a get_cust_info() or similar to allow customer to enter his/her information or just define them in
__init__() and pass customer information as arguments while creating a customer object.

__str__(): Print customer information and price nicely. Find a way to link two classes. 
For example, instances of both classes may have a customer number. With a get method, 
get the customer number and pass it to the item object as an argument to set customer 
number attribute. So Customer class instance holds the customer info, Items class holds the
shopped item's info for the same customer ID number such as price, quantity or so. 

In the end, print both info (customer info and shopped items info) using their respective str format in a nice
way.

Simple example:
Customer1 = [name : Jack, last_name : Russel, customer_id : 123]
shopping_cart1 = [customer_id: 123, items : [necklace, ring, ear ring], total_price : 2000, discount : 300,
price_tobe_paid: 1700]

Crate a few customers and print their information (Personal and shopping info)."""

from functools import reduce

#CUSTOMER INFO
class Customer():
    def __init__(self, name, lastname, customer_id):
        self.name = name
        self.lastname = lastname
        self.customer_id = customer_id

    @classmethod
    def get_cust_info(cls, cust_info):
        name, lastname, customer_id = cust_info.split(",")
        return cls(name, lastname, customer_id)

    def __str__(self):
        return f"Customer Name: {self.name} {self.lastname}\nCustomer ID: {self.customer_id}"

#ITEMS INFO
class Items():
    cart = []
    product_list= {"Carolina Herrera": 200, "Gucci": 220, "Versace": 250, "Prada": 280, "Tous": 170, "Burberry": 210, "Louis Vuitton": 290, "Dolce & Gabbana": 300, "JW Anderson": 220}
    ### we should send the list after the creation of the class, not in the class. 
    ### we can create an empty list or a cart, bur we can use them after class creation, that's the aim of OOP.

    def __init__(self, customer_id, items, total_price):
        self.customer_id = customer_id
        self.items = items
        self.total_price = total_price

        self.discount = self.calculate_discount()
        self.price_to_be_paid = self.get_total_amount()

    def __str__(self):
        print (f"Customer ID: {self.customer_id}\nItems: {self.items}\nTotal Price: {self.total_price}\nDiscount: {self.discount}\nTotal Price to be Paid: {self.price_to_be_paid}")

    def calculate_discount(self):
        if self.total_price >= 4000:
            self.discount = 25
        elif self.total_price >= 2000:
            self.discount = 15
        elif self.total_price < 2000:
            self.discount = 10
        return self.discount

    def get_total_amount(self):
        self.price_to_be_paid = self.total_price - (self.total_price * self.discount/100)
        return self.price_to_be_paid

    def shopping_cart(self):
        print("PRODUCTS AND PRICES ")
        print({"Carolina Herrera": 200, "Gucci": 220, "Versace": 250, "Prada": 280, "Tous": 170, "Burberry": 210, "Louis Vuitton": 290, "Dolce & Gabbana": 300, "JW Anderson": 220})
        while True:
            self.product = input("Product to add Cart: ")
            self.qty = int(input("Number of products to add: "))
            self.cart.append([self.product, self.qty])
            print(f"Updated list: {self.cart}")
            
            
            self.exit = (input("Do you want to add new item? Y(yes) or N(no): ")).upper()
            if self.exit == "Y":
                continue
            elif self.exit == "N":
                break

            def product_price(**product_list):
                for product in self.product_list.keys():
                    self.product_price = self.product_list.values()
                    self.total_price = self.product_price * self.qty
                    return self.total_price
        
        self.result = reduce(product_price(), self.cart)
        print (f"Total price of the cart: {self.result}") 


class Common(Customer,Items):
    def __init__(self):
        Customer.__init__(self)
        Items.__init__(self)
    
    def customer_item_info(cust, item):
        if cust.customer_id == item.customer_id:
            print(f"Customer: {cust.name} {cust.lastname}, ID: {cust.customer_id}")
            print(f"Items: {item.items}, Total Price: {item.total_price}, Discount: {item.discount}, Price to Pay: {item.price_to_be_paid}")
        else: 
            print("ID is not matched..")


cust1 = Customer ("Melike", "Kaya", "MK123")
cust2 = Customer.get_cust_info("Said,Kardic,SK678")
# print(cust2.__str__())

item1 = Items("MK123", ["bag", "neclace"], 2700)
item2 = Items("User123", ["Carolina Herrera", "Gucci", "Versace"], 4800)
item3 = Items("SK678", ["watch", "cologne", "cap", "pants"], 6700)

# item1.shopping_cart()
# item1.__str__()
# item2.__str__()

Common.customer_item_info(cust1, item1)
Common.customer_item_info(cust2, item3)

### We can take the inputs from the users.
### We didn't need to create the third class, we were able to 
### well done