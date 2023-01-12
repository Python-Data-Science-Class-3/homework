
"""
Question 3:
Define a class named Product with the following specifications:
Data members:
• product_id - A string to store product.
• product_name - A string to store the name of the product.
• product_purchase_price - A decimal to store the cost price of the product.
• product_sale_price - A decimal to store Sale Price 
• Margin - A decimal to be calculated as (product_sale_price - product_purchase_price)
• Remarks - To store "Profit" if Margin is positive else "Loss" if Margin is negative.
Methods:
• A constructor to intialize all the data members with valid default values.
• A method set_remarks() that assigns Margin as (product_sale_price - product_purchase_price) and sets
Remarks as mentioned below :

Margin         Remarks
<O (negative)   Loss
>0 (positive)   Profit

• A method set_details() to accept values for product_id, product_name, product_purchase_price,
product_sale_price and invokes SetRemarks() method.
• A method get_details() that displays all the data members.
"""

class Product():
       
    def __init__(self,product_id="",product_name="",product_purchase_price=0.0,product_sale_price=0.0) -> None:
       
        # self.set_details()
        self.product_id = product_id
        self.product_name =product_name 
        self.product_purchase_price = product_purchase_price
        self.product_sale_price =product_sale_price
        
    def set_remarks(self):
        self.margin =self.product_sale_price -self.product_purchase_price 
        if self.margin<0:
            return "Loss"
        if self.margin>0:
           return "Profit"
        else:
            return "0"


    def set_details(self):
        self.product_id = int(input("Enter Product ID: "))
        self.product_name = str(input("Enter Product Name: "))
        self.product_purchase_price = float(input("Enter Product Purchase Price: "))
        self.product_sale_price = float(input("Enter Product Sale Price: "))
        #We set to self.remark the sent value of self.set_remarks .
        self.remark =self.set_remarks()  




    def get_details(self):
       
        # With this    __dict__      method, we have created a dictionary by matching the properties of our object with their values.
        data = self.__dict__ 
        print('\n')
        print("Our product details :")
        print("-"*100)
        print(f'{data}')
        print("-"*100)


new_product = Product()
new_product.set_details()
new_product.set_remarks()
new_product.get_details()

    
    


    

    

        
                
        



           


