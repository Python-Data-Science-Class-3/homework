'''Developer : Tuba GÜMÜS ESMEK
   Date      : 06.01.2023
   Subject   : Customer

'''
#Write a Customer class and Items class. Let user enter customer information and add stuff to his/her shopping card.
#Class Items : Method : __init__(), __str__(), calculate_discount(), shopping_cart(), get_total_amount()
#calculate_discount():
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
#Crate a few customers and print their information (Personal and shopping info).

class Customer:
    Shopping_cart = []
    def __init__(self,name, last_name,customer_id):
        self.name = name
        self.last_name = last_name
        self.customer_id = customer_id
    def get_cust_info(self):
        self.name = input("Please,Write your name: ")
        self.last_name = input("Please,Write your Last_name: ")
        self.customer_id = input("Please, Write your Customer_ID : ")

    def __str__(self):
        return "name : {} last_name : {} customer_id : {}".format(self.name, self.last_name, self.customer_id)

#customer1 = Customer("Tuba", "Esmek","123DE")
#customer2 = Customer("Yeliz","Kaya","klmDE")
#customer3 = Customer("Selim", "Yildirim","456DE")
class Items(Customer):
    def __init__(self,name, last_name,customer_id,price, qty, shopped_items):
        super().__init__(name, last_name, customer_id)
        self.price = price
        self.qty =qty
        self.shopped_items = shopped_items
        self.customer_id= customer_id

    def shopping_cart(self):
        Customer.Shopping_cart.append([self.customer_id,self.shopped_items, self.price, self.qty])
   
    def calculate_discount(self):
        
        self. total_price = self.price * self.qty
        if self.total_price >= 4000:
            self.discount = 0.25
        elif self.total_price >= 2000:
            self.discount = 0.15
        else:
            self.discount = 0.10

    def get_total_amount(self):
        self.price_tobe_paid = self.total_price-self.discount

    def __str__(self):
        return "shoppng_cart [customer_id :{} shopped_items : {} total_price : {} discount : {} price_tobe_paid ; {}]".format(self.customer_id,self.shopped_items,self.total_price,self.discount, self.price_tobe_paid)
        

customer1= Customer
print(customer1.get_cust_info)