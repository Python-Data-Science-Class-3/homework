'''Developer : Tuba GÜMÜS ESMEK
   Date      :05.01.2023
   Subject   : Product

'''


#Define a class named Product with the following specifications:
#Data members:
#- product_id – A string to store product.
#- product_name - A string to store the name of the product.
#- product_purchase_price – A decimal to store the cost price of the product.
#- product_sale_price – A decimal to store Sale Price Margin - A decimal to be calculated as (product_sale_price - product_purchase_price)
#- Remarks - To store "Profit" if Margin is positive else "Loss" if Margin is negative.
#Methods :
##- A constructor to intialize all the data members with valid default values.
#- A method set_remarks() that assigns Margin as (product_sale_price - product_purchase_price) and sets Remarks as mentioned below :
#- Margin	Remarks
   # <0 (negative)	Loss
    #>0 (positive)	Profit
#- A  set_details() to accept values for product_id. product_name, product_purchase_price, product_sale_price and invokes SetRemarks() method.
#- A method get_details() that displays all the data members.'method

class Product:     ##creating the  class Society

   ##creating objects with the init method
    def __init__(self,product_id= None, product_name=None, product_purchase_price=0, product_sale_price=0, margin= 0):
        self.product_id = product_id
        self.product_name = product_name
        self.product_purchase_price = float(product_purchase_price)
        self.product_sale_price = float(product_sale_price)
        self.margin= margin
    #using if loop to show result of remarks based on Margin value with set-remarks method    
    def set_Remarks(self):
        self.margin = self.product_sale_price - self.product_purchase_price  
        if self.margin <0:
            self.remarks = "PROFIT"
        else:
            self.remarks = "LOSS"
         
     # getting data from user with set_details method  
    def set_details(self):
        self.product_id = input("Product_id:")
        self.product_name = input("Product_name: ")
        self.product_purchase_price =float(input("Product_Purchase:"))
        self.product_sale_price = float(input("Product_Sale:"))
        self.flat = "D Type"
        self.flat = "D Type"
        self.flat = "D Type"
     # using show_all method to show the all data members 
    def get_details(self):
        return "product_id: {} product_name: {} product_purchase_price: {} product_sale_price : {} remarks: {}". format(self.product_id, self.product_name,self. product_purchase_price ,self.product_sale_price, self.remarks)
        #return f' Product ({self.product_name}, {self.product_purchase_price}, {self.product_sale_price},  {self.remarks})'
        
        


items1 = Product()
items1.set_details()
items1.set_Remarks()
print(items1.get_details())