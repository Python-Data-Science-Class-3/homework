
'''
---PROJECT---
Define a class named Product with the following specifications:
Data members:
- product_id – A string to store product.
- product_name - A string to store the name of the product.
- product_purchase_price – A decimal to store the cost price of the product.
- product_sale_price – A decimal to store Sale Price Margin - A decimal to be calculated as (product_sale_price - product_purchase_price)
- Remarks - To store "Profit" if Margin is positive else "Loss" if Margin is negative.
Methods :
- A constructor to intialize all the data members with valid default values.
- A method set_remarks() that assigns Margin as (product_sale_price - product_purchase_price) and sets Remarks as mentioned below :
- Margin	Remarks
    <0 (negative)	Loss
    >0 (positive)	Profit
- A method set_details() to accept values for product_id. product_name, product_purchase_price, product_sale_price and invokes SetRemarks() method.
- A method get_details() that displays all the data members.
'''




class product(): 
    def __init__(self,product_id = 0,product_name = 0, product_purchase_price = 0, product_sale_price = 0): 
        self.product_id = product_id 
        self.product_name = product_name 
        self.product_purchase_price = product_purchase_price 
        self.product_sale_price = product_sale_price 
        # self.product_margin = product_sale_price - product_purchase_price 
    def set_remarks(self): 
        if self.product_sale_price - self.product_purchase_price > 0: 
            self.remarks = "Profit" 
        else : 
            self.remarks = "Loss" 
    def set_details(self): 
        self.product_id = input("Product id :") 
        self.product_name = input("Product name :") 
        self.product_purchase_price = int(input("Purchase price :")) 
        self.product_sale_price = int(input("Sale price :")) 
    def get_details(self): 
        print("You have made a " + self.remarks + " from the product with this id :" + self.product_id + " with this name  " + self.product_name) 
sale1 = product() 
sale1.set_details() 
sale1.set_remarks() 
sale1.get_details() 