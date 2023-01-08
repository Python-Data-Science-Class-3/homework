#Define a class named Product with the following specifications:
#Data members:
#product_id – A string to store product.
#product_name - A string to store the name of the product.
#product_purchase_price – A decimal to store the cost price of the product.
#product_sale_price – A decimal to store Sale Price Margin
#A decimal to be calculated as (product_sale_price - product_purchase_price)
#Remarks - To store "Profit" if Margin is positive else "Loss" if Margin is negative.
#Methods :
#A constructor to intialize all the data membe1rs with valid default values.
#A method setRemarks() that assigns Margin as (product_sale_price - product_purchase_price)and sets Remarks as mentioned below :
#Margin	Remarks <0 (negative)	Loss >0 (positive)	Profit
#A method set_details() to accept values for product_id. product_name, product_purchase_price, product_sale_price and invokes SetRemarks() method.
#A method get_details() that displays all the data members.


class Product:
    def __init__(self,product_id = '', product_name = '', product_purchase_price = 0, product_sale_price = 0):
      self.product_id = product_id
      self.product_name = product_name
      self.product_purchase_price = product_purchase_price
      self.product_sale_price = product_sale_price
      ### good initial values, you can try to choose float number for prices (0.0)
      ### type(0) ---> int /// type(0.0) ---> float
      
      
    def setRemarks(self):          # A method that assigns Margin as (product_sale_price - product_purchase_price)
        ### set_remarks !!!

        ### Where did you create self.remarks?
        ### There is no self.remarks object in the class.
        ### I have seen it in the following function, but if you won't call set_details but only setRemarks,
        ### then it's 
        if self.remarks < 0 :
             return "Loss"
        elif self.remarks > 0 : 
             return "Profit"
        else:
            print("Neither Profit Nor Loss")     

    def set_details(self):          # A method set_details() to accept values for data members
        self.product_id = input("Enter product id: ")     
        self.product_name = input("Enter product name: ")
        self.product_purchase_price = float(input("Enter product purchase price: "))
        self.product_sale_price = float(input("Enter product sale price: ")) 
        self.remarks = self.product_sale_price - self.product_purchase_price # calculated as (product_sale_price - product_purchase_price)

    def get_details(self):        #A method get_details() that displays all the data members
        print(f"\nProduct Id: {self.product_id}\nProduct Name: {self.product_name}"
        f"\nProduct Purchase Price: {self.product_purchase_price}\nProduct sale  price: {self.product_sale_price}\nProduct Remarks: {self.setRemarks()}")


product = Product()
product.set_details()
print(product.get_details())

### You can take a look at the following example

"""
class Product:

    def __init__(self, product_id = None, product_name = None, product_purchase_price = 0.0, product_sale_price = 0.0):
        self.product_id = product_id
        self.product_name = product_name
        self.product_purchase_price = product_purchase_price
        self.product_sale_price = product_sale_price

    def set_remarks(self):
        self.margin = self.product_sale_price - self.product_purchase_price
        
        if self.margin > 0:
            print("Profit")
        
        elif self.margin < 0:
            print("Loss")

        else:
            print("Neither Profit Nor Loss")



product_1 = Product(product_purchase_price = 35.5, product_sale_price = 45)
product_1.set_remarks()

product_2 = Product(product_purchase_price = 45, product_sale_price = 45)
product_2.set_remarks()
"""


