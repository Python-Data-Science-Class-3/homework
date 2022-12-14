'''
Define a class named Product with the following specifications:
Data members:
•	product_id — A string to store product.
•	product_name - A string to store the name of the product.
•	product_purchase_price — A decimal to store the cost price of the product.
•	product_sale_price —A decimal to store Sale Price Margin - A decimal to be calculated as (product_sale_price – product_purchase_price)
•	Remarks - To store "Profit" if Margin is positive else "Loss" if Margin is negative.
Methods :
•	A constructor to intialize all the data members with valid default values.
•	A method set_remarks() that assigns Margin as (product_sale_price -  product_purchase_price) and sets Remarks as mentioned below :
'''
class Product():     #cerate a class with name'Product'
    def __init__(self,product_id,product_name,product_purchase_price,product_sale_price):
        self.product_id=product_id
        self.product_name=product_name
        self.product_purchase_price=product_purchase_price
        self.product_sale_price=product_sale_price

    def set_remarks(self):    #create a func to know margin
        if (self.product_sale_price-self.product_purchase_price)>0:
            return "Profit"
        else:
            return "Loss" 
    def input_details(self):    #create a func to take inputs
        try:
            self.product_id = input("Enter id of product ? ")
            self.product_name = input("Enter name of product ? ")
            self.product_purchase_price = int(input("Enter product purchase price ? "))
            self.product_sale_price = int(input("Enter product sale price ? "))

        except:
            print("Please enter the values str for id and name and enter the values int for prices correctly  ")
          
    def show_details(self):
        print (f"""
----------Details------------        
Product ID             : {self.product_id}
Product name           : {self.product_name}
Product purchase price : {self.product_purchase_price}
Product sale price     : {self.product_sale_price}
Sale price margin      : {Product.set_remarks(self)} """)   #get the func remarks

product_1=Product('','',0,0)      #create an object
product_2=Product('','',0,0)

        
product_1.input_details()         #take inputs
product_1.show_details()          #see details

product_2.input_details()
product_2.show_details()

