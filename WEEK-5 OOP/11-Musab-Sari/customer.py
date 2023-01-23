"""
Developer   : Musab SARI
Date        : 23.01.2023

Question 4: 
Write a customer class and Items class. Let user enter customer information and add stuff to his/her shopping card.
Class Items : Method : _init_(}, _str _(} , calculate_discount(} , shopping_cart(} , get_total_amount() calculate_discountO: 
•	total_price = price * qty
•	discount-> 25% if total_price >= 4000
•	discount-> 15% if total_price >= 2000
•	discount-> 10% if total_price < 2000
•	price_ tobe_paid = total_price - discount

shopping_cartQ: 
Let user add items in the shopping basket. Be creative with the items, set their prices as well. 

_str_(}: 
•	Print items added and total price nicely. Class Customer: Methods: _init_(} ·', get_cust_info() this is optional, str()'
Optionally create a get_cust_info() or similar to allow customer to enter his/her information or just define them in _init_() 
and pass customer information as arguments while creating a customer object. 
_str_(): 
Print customer information and price nicely. Find a way to link two classes. For example, instances of both classes may
have a customer number. With a get method, get the customer number and pass it to the item object as an argument to set 
customer number attribute. So customer class instance holds the customer info, Items class holds the shopped item's info 
for the same customer ID number such as price, quantity or so. 

In the end, print both info (customer info and shopped items info) using their respective _str_ format in a nice way. 

Simple example: 
Customer1 = [name : Jack, last_name: Russel, customer_id: 123] 

shopping_cartl = [customer_id : 123, items : [necklace, ring, ear ring], total_price 2000, discount 300, price_tobe_paid : 1700] 
Crate a few customers and print their information (Personal and shopping info). 
"""

class Customer:
    customerID = None
    def __init__(self, name = None, surname = None, customer_id = int()):
        self.name = name
        self.surname = surname
        self.customer_id = customer_id
        
    def user_input(self):
        self.name = input("Name:")
        self.surname = input("Surname:")
        self.customer_id = int(input("Customer ID:"))
        Customer.customerID = self.customer_id
        return self.name, self.surname, self.customer_id
    
    def __str__(self):
        print(f"\nName:{self.name}\nSurname:{self.surname}\nCustomer ID:{self.customer_id}")
        

class Item:
    user_item_list = []
    user_items_price_list = []
    def __init__(self,  price = None, qty = None, total_price = None, discount = None):
        self.price = price
        self.qty = qty
        self.total_price = total_price
        self.discount = discount

    def __str__(self):
        print(f"\nCustomer ID:{Customer.customerID}\nItems:{self.user_item_list}\nTotal Price:{self.total_price}\nDiscount:{self.discount_amount}\nPrice to be Paid:{self.price_to_be_paid}")

    def calculate_discount(self):

        if self.total_price >= 4000:
            self.discount = 0.25

        elif self.total_price >= 2000 and self.total_price < 4000:
            self.discount = 0.15

        elif self.total_price < 2000:
            self.discount = 0.1

        self.price_to_be_paid = self.total_price*(1-self.discount)
        self.discount_amount = self.total_price*self.discount

        return self.price_to_be_paid, self.discount_amount

    def shopping_cart(self):
        print(itemlist)
        user_selection = int(input("Please pick the item you want by pressing the number in front:"))
        
        for i in range(len(item_dic)):
        
            if i == (user_selection - 1):
                self.user_item_list.append(item_dic[i][0])
                self.qty = int(input(f'For {item_dic[i][0]}, how many do you want: '))
                self.price = (item_dic[i][1])*self.qty
                self.user_items_price_list.append(self.price)        
        
        return self.user_item_list, self.qty, self.user_items_price_list                                                             
    
    def get_total_amount(self):
        self.total_price = sum(self.user_items_price_list)

        return self.total_price

item_dic = [["iPhone 15 Pro Max",2199], ["Samsung Galaxy XXII",1899], ["Xiaomi RedMi Note 15 Pro",1599], ["Nokia 1110",19], ["Sony Xperia 11",1699]]
itemlist = """1 - ["iPhone 15 Pro Max",2199]
2 - ["Samsung Galaxy XXII",1899]
3 - ["Xiaomi RedMi Note 15 Pro",1599]
4 - ["Nokia 1110",19]
5 - ["Sony Xperia 11",1699]"""
customers = Customer()
selections = Item()

customers.user_input()
selections.shopping_cart()
selections.get_total_amount()
selections.calculate_discount()


while True:
    UserChoice = input("""Would you like to add more items?
    Press Y to continue
    Press N to go checkout
    Answer: """).lower()
    try:
        
        UserChoice == "y" or "n"

    except:
        
        print("Wrong Entry!")
        
    else:
        
        if UserChoice == "y":
            
            selections.shopping_cart()
            selections.get_total_amount()
            selections.calculate_discount()
        
        else:
        
            break
    
    
customers.__str__()
selections.__str__()