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
margin<0 Loss margin>0 Profit
A method set_details() to accept values for product_id.product_name, product_purchase_price, product_sale_price and invakes SetRemarks() method.
A method get_details() that displays all the data members.
'''
import json
class Product:
    productAll = {}
    record = 0
    def __init__(self,product_id=int(), product_name="", product_purchase_price=int(), product_sale_price=int()):
        Product.record += 1
        # self.itemRecordOrder = Product.record
        self.product_id = product_id
        self.product_name = product_name
        self.product_purchase_price = product_purchase_price
        self.product_sale_price = product_sale_price
        self.set_details()
        self.set_remarks()
        self.addAll()
        self.get_details()

    def set_remarks(self):
        self.margin = self.product_sale_price - self.product_purchase_price  
        if self.margin < 0:
            # return "Loss"
            self.margin = "Loss"
        elif self.margin > 0:
            # return "Profit"
            self.margin = "Profit"
        else:
            pass
        
    def set_details(self):
        self.product_id = int(input("enter product id to add a new one: "))
        self.product_name = input("enter product name: ")
        self.product_purchase_price = int(input("enter product purchase prise: "))
        self.product_sale_price = int(input("enter product sale price: "))    
        self.set_remarks()
    
    def addAll(self):
        Product.productAll["Product Recording Order "+ str(Product.record)] = self.__dict__  
    @classmethod
    def get_details(cls):
        print(json.dumps(Product.productAll, indent= 5))
        print("\n")
        print("\n")   
        print("you can add new product below ↓")
        

allEntity = []
while True:
    newEntity = Product()
    newEntity.set_details
    allEntity.append(newEntity)