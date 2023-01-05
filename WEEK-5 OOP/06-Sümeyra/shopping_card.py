#Write a Customer class and Items class. Let user enter customer information and add stuff to his/her shopping card.
#Class Items : Method: __init__(), __str__(), calculate_discount(), shopping_cart(), get_total_amount() :
#total_price = price * qty
#discount —> 25% if total_price >= 4000
#discount —> 15% if total_price >= 2000
#discount —> 10% if total_price < 2000
#price_tobe_paid = total_price – discount
#shopping_cart():
#Let user add items in the shopping basket. Be creative with the items, set their prices as well.
#__str__():
#Print items added and total price nicely. Class Customer : Methods: __init__()``, get_cust_info()this is optional,str()`
#Optionally create a get_cust_info() or similar to allow customer to enter his/her information or just define them in __init__() and pass customer information as arguments while creating a customer object.
#__str__():
#Print customer information and price nicely. Find a way to link two classes. For example, instances of both classes may have a customer number. With a get method, get the customer number and pass it to the item object as an argument to set customer number attribute. So Customer class instance holds the customer info, Items class holds the shopped item’s info for the same customer ID number such as price, quantity or so.
#In the end, print both info (customer info and shopped items info) using their respective __str__ format in a nice way.
#Simple example:
#Customer1 = [name : Jack, last_name : Russel, customer_id : 123]
#shopping_cart1 = [customer_id : 123, items : [necklace, ring, ear ring], total_price : 2000, discount : 300, price_tobe_paid : 1700]
#Crate a few customers and print their information (Personal and shopping info)."""

class Customer:
    def __init__(self):                      # user enter customer information
        self.name = input("Name: ")
        self.last_name = input("Last Name:  ")
        self.customer_ID = input("Customer ID: ")
        
    
    def __str__(self):
        return f"name : {self.name}\nlast_name : {self.last_name}\ncustomer_id : {self.customer_ID}" 

class Items(Customer):
    

    def __init__(self):
        super().__init__()

    

    def shopping_cart(self):                #user add stuff to his/her shopping card
        self.items = []
        self.prices = []
        while(True):
            self.item = input("Enter item name :")
            self.items.append(self.item)
            self.price =int(input("Enter the price of this product: "))
            self.qty =int(input("Enter how many of this product you will buy: "))
            self.prices.append([self.price,self.qty])
            self.answer = input("\nPress 'a' to add new product:\nPress 'f' to end the transaction:\n")
            if self.answer == "a":
                continue
            elif self.answer == "f":
                break
     
    
    
    def calculate_discount(self):
        self.price_tobe_paid = 0
        self.total_price = 0
        self.total_item_price = self.price * self.qty
        self.total_price += self.total_item_price
            
        if self.total_price >= 4000:
            self.discount = 0.25
        elif self.total_price >= 2000:
            self.discount = 0.15
        elif self.total_price < 2000:
            self.discount = 0.10
        
        self.total_discount = self.total_price * self.discount
        self.price_tobe_paid = self.total_price - (self.total_discount) 
    
        def __str__(self):
          return f"Costumer Name : {self.name} Costumer Last Name : {self.last_name} Customer ID: {self.customer_ID}\nItems = {self.items} Total Price = {self.total_price} Discount: {self.total_discount} Price Tobe Paid: {self.price_tobe_paid}"

    
    


costumer1 = Items()
costumer1.shopping_cart()
costumer1.calculate_discount()
print(costumer1)