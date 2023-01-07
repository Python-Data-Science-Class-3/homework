""" 

Developer : Melih Orhan Yilmaz
Date      : 04.01.2023

Application : Product OOP

Explanation : 
Define a class named Product with the following specifications:
Data members:
product_id – A string to store product.
product_name - A string to store the name of the product.
product_purchase_price – A decimal to store the cost price of the product.
product_sale_price – A decimal to store Sale Price Margin
A decimal to be calculated as (product_sale_price - product_purchase_price)
Remarks - To store "Profit" if Margin is positive else "Loss" if Margin is negative.
Methods :
A constructor to intialize all the data members with valid default values.
A method setRemarks() that assigns Margin as (product_sale_price - product_purchase_price)and sets Remarks as mentioned below :
Margin	Remarks <0 (negative)	Loss >0 (positive)	Profit
A method set_details() to accept values for product_id. product_name, product_purchase_price, product_sale_price and invokes SetRemarks() method.
A method get_details() that displays all the data members.

"""

class Product():
    
    def __init__(self): # All the data members with valid default values
        self.id = ""
        self.name = ""
        self.purchase = 0
        self.sale = 0
        self.margin = 0
        self.remarks = ""
    
    def SetRemarks(self):
        self.margin = self.sale - self.purchase
        if self.margin > 0:
            self.remarks = "Profit"
        else:
            self.remarks = "Loss"

    def SetDetails(self): # Get input from the user
        while True:
            try:
                self.id = int(input("Enter product ID: "))
                self.name = input("Enter product name: ")
                self.sale = int(input("Enter product selling price: "))
                self.purchase = int(input("Enter product purchase price: "))
                self.SetRemarks() # Call SetRemarks

                return self.id, self.name, self.sale, self.purchase

            except:
                print("Invalid. Please enter new value.")

    def GetDetails(self): # Show all the data members
        print(f"Product ID: {self.id}\nProduct Name: {self.name}\nProduct Sale: {self.sale}\nProduct Purchase: {self.purchase}\nProduct Margin: {self.margin}\nProduct Remark: {self.remarks}")

product1 = Product()
product1.SetDetails()
product1.GetDetails()