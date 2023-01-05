#Define a class named Product with the following specifications:
# Data members:
# product_id – A string to store product.
# product_name - A string to store the name of the product.
# product_purchase_price – A decimal to store the cost price of the product.
# product_sale_price – A decimal to store Sale Price Margin - A decimal to be calculated as (product_sale_price - product_purchase_price)
# Remarks - To store "Profit" if Margin is positive else "Loss" if Margin is negative.
# Methods :
# A constructor to intialize all the data members with valid default values.
# A method set_remarks() that assigns Margin as (product_sale_price - product_purchase_price) and sets Remarks as mentioned below :
# <0 (negative) Loss  and >0 (positive) Profit
# A method set_details() to accept values for product_id. product_name, product_purchase_price, product_sale_price and invokes SetRemarks() method.
# A method get_details() that displays all the data members.


class Product:
    def __init__(self, product_id = " ", product_name= " ", product_purchase_price = 0 , product_sale_price = 0):
        self.product_id = product_id
        self.product_name = product_name
        self.product_purchase_price = product_purchase_price
        self.product_sale_price = product_sale_price

    def set_remarks(self):                                                          #a method to calculate the product status "Loss" or "Profit"
        if (self.product_sale_price- self.product_purchase_price) < 0 :
            return "Loss"
        else :
            return "Profit"

    def set_details(self):                                                          #a method to enter the values about product
        try : 
            self.product_id = input("Please enter the Prodcut ID:  ")
            self.product_name = input("Please enter the Product Name:  ")
            self.product_purchase_price = int(input("Please enter the Product Purchase Price:  "))
            self.product_sale_price = int (input("Please enter the Product Sale Price:  "))
        
        except ValueError :                                                         #an except for to catch the ValueError
            print("Please enter a number")
            return self.set_details()

    def get_details(self):                                                          #a method to display all te data of members
        print (f"""
        Product ID              : {self.product_id}
        Product Name            : {self.product_name}
        Product Purchase Price  : {self.product_purchase_price}
        Product Sale Price      : {self.product_sale_price}
        Product Remarks Status  : {Product.set_remarks(self)}        
        """)


entry_new = Product()                                                           # sending a new antry
entry_new.set_details()                                                         #calling set_dateials method
entry_new.set_remarks()                                                         #calling  get_details method
entry_new.get_details()

