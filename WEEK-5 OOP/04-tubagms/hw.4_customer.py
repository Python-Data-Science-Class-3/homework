'''Developer : Tuba GÜMÜS ESMEK
   Date      : 12.01.2023
   Subject   : Customer Class / Items class

'''
# Write a Customer class and Items class. Let user enter customer information and add stuff to his/her shopping card.
# Class Items : Method : __init__(), __str__(), calculate_discount(), shopping_cart(), get_total_amount()
# calculate_discount():
# total_price = price * qty
# discount —> 25% if total_price >= 4000
# discount —> 15% if total_price >= 2000
# discount —> 10% if total_price < 2000
# price_tobe_paid = total_price – discount
# shopping_cart():
# Let user add items in the shopping basket. Be creative with the items, set their prices as well.
# __str__():
# Print items added and total price nicely. Class Customer : Methods: __init__()``, get_cust_info()this is optional,str()`
# Optionally create a get_cust_info() or similar to allow customer to enter his/her information or just define them in __init__() and pass customer information as arguments while creating a customer object.
# __str__():
# Print customer information and price nicely. Find a way to link two classes. For example, instances of both classes may have a customer number. With a get method, get the customer number and pass it to the item object as an argument to set customer number attribute. So Customer class instance holds the customer info, Items class holds the shopped item’s info for the same customer ID number such as price, quantity or so.
# In the end, print both info (customer info and shopped items info) using their respective __str__ format in a nice way.
# Simple example:
# Customer1 = [name : Jack, last_name : Russel, customer_id : 123]
# shopping_cart1 = [customer_id : 123, items : [necklace, ring, ear ring], total_price : 2000, discount : 300, price_tobe_paid : 1700]
# Crate a few customers and print their information (Personal and shopping info).
# '''
class Customer:           ##creating the  class Customer
    #creating objects with the init method
    def __init__(self,cust_name, cust_Lastname, customer_ID):
        self.cust_name = cust_name
        self.cust_Lastname = cust_Lastname
        self.customer_ID = customer_ID
     #getting data from user with get_cust_info method 
    def get_cust_info(self):
        self.cust_name = input("Please write your name : ")
        self.cust_Lastname = input("Pleasee Write your Lastname : ")
        self.customer_ID = input("Please Write your Customer_ID : ")
#Printing  customer information and price nicely with __str__ method
    def  __str__(self):
           
       print (f'[Name : {self.cust_name}---- Lastname : {self.cust_Lastname}---- ID : {self.customer_ID}]')   
    
#creating the  class Items for shopping information  and creating objects with the init method         
class Items:           
   
    def __init__(self,price,customer_ID):
        self.price = price
        self.customer_ID = customer_ID
 
#Creating a shopping_cart method for the user to add products to the shopping cart and for price and quantity information       
    def shopping_cart(self):   
        self.shopping_list = [] 
        self.shopping_price = []      
        
        self.customer_ID = input("Please Write your Customer_ID : ")
        
#The process continues until the shopping process is exited with the while loop. 
        while True: 

           self.item = input("Please, Add your item  :")
           self.shopping_list.append(self.item)
           self.qty = int(input("Please, Chooce your qty : "))
           self.price = int(input(" Please, Write price : "))
           self.shopping_price.append(self.price)
           self.choice = input("If You Want to Continue Shopping : 'Y'\n  for EXIT : 'Q' ")
           if self.choice == "Y" :
                 continue

           else:

                break
            
        self.calculate_discount()
        self.get_total_amount()
      
 # Determining the discount on the total price by calculating the price and quantity information    
    def calculate_discount(self):
        self.total_price = float(self.price) * int(self.qty)
        self.shopping_price = self.total_price
       
        if self.total_price >= 4000:
            self.discount = 0.25
        elif self.total_price >= 2000:
            self.discount =0.15
        else:
            self.discount = 0.10
 # Total price with get_total_amount method  
    def get_total_amount(self):   
        self.price_tobe_paid= (self.total_price) - (self.total_price*self.discount)
        return self.price_tobe_paid

# Printing customer information and price nicely.        

    def __str__(self):
     #return "customer_ID : {}\n items : {} \n total_price : {}\n discount : {}\n  Price_tobe_paid : {}".format(self.customer_ID, self.item, self.total_price,self.discount, self.get_total_amount())
     return f"[Customer_ID : {self.customer_ID} .  item :{self.shopping_list}  Total_price : {self.shopping_price} discount : {self.discount}, Net_price : {self.price_tobe_paid}]"
   

    

customer1= Customer(" ", " ", " ")
customer1.get_cust_info()
customer1.__str__()

item_1 = Items("0", " ")
item_1.shopping_cart()
item_1.calculate_discount()
item_1.get_total_amount()


print(item_1)




