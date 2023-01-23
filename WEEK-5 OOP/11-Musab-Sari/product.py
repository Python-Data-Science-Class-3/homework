"""
Developer   : Musab SARI
Date        : 23.01.2023

Question 3: 
Define a class named Product with the following specifications: 

Data members: 

• 	product_id - A string to store product.
• 	product_name - A string to store the name of the product.
• 	product_purchase_price - A decimal to store the cost price of the product.
•	product_sale_price - A decimal to store Sale Price Margin - A decimal to be calculated as (product_sale_price -	product_purchase_price) 
•	Remarks - To store "Profit" if Margin is positive else "Loss" if Margin is negative.

Methods :
•	A constructor to intialize all the data members with valid default values.
•	A method set_remarks() that assigns Margin as (product_sale_price - product_purchase_price) and sets Remarks as mentioned below :
Margin           Remarks
<0 (negative)    Loss
>0 (positive)    Profit

•	A method set_details() to accept values for product_id . product_name , product_purchase_price , product_sale_price and invokes SetRemarks() method.
•	A method get_details() that displays all the data members.

"""

class Product:

    def __init__(self, product_id = None, product_name = None, product_purchase_price = None, product_sale_price = None, product_sale_price_margin = None, remarks = None):
        self.product_id = product_id
        self.product_name = product_name
        self.product_purchase_price = product_purchase_price
        self.product_sale_price = product_sale_price
        self.product_sale_price_margin = product_sale_price_margin
        self.remarks = remarks

    def set_remarks(self):
        self.product_sale_price_margin = self.product_sale_price - self.product_purchase_price

        if self.product_sale_price_margin > 0:
            self.remarks = "Profit"

        elif self.product_sale_price_margin < 0:
            self.remarks = "Loss"

        else:
            self.remarks = "Even"

        return self.remarks

    def set_details(self):
        self.product_id = input("Product ID:")
        self.product_name = input("Product Name:")
        self.product_purchase_price = float(input("Purchase price of the product:"))
        self.product_sale_price = float(input("Sale price of the product:"))
        self.remarks = Product.set_remarks(self)

        return self.product_id, self.product_name, self.product_purchase_price, self.product_sale_price, self.remarks

    def get_details(self):

        print(f"\nProduct ID:{self.product_id}\nProduct Name:{self.product_name}\nProduct Purchase Price:{self.product_purchase_price}\nProduct Sale Price:{self.product_sale_price}\nProduct Sales Price Margin:{self.product_sale_price_margin}\nRemarks:{self.remarks}")

products = Product()

while True:

    products.set_details()
    products.get_details()
    newproduct = input("Would you like to add new product?\nPress Y/N: ").upper()

    if newproduct == "Y":

        print("Processing...")

    else:

        break