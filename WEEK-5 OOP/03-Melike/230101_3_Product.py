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
    product_list = []
    def __init__(self, product_id = "default_id", product_name = "default_product", product_purchase_price = 0.0, product_sale_price = 0.0):
        ### Good initial values
        self.product_id = product_id
        self.product_name = product_name
        self.product_purchase_price = product_purchase_price
        self.product_sale_price = product_sale_price

        self.margin = self.product_sale_price - self.product_purchase_price
        self.remarks = self.set_remarks()

        Product.product_list.append([self.product_id, self.product_name, self.product_purchase_price, self.product_sale_price, self.margin, self.remarks])
        ### I have tried to explain the same issue for other problems. You can take a look there.

    def display_product(self):
        print(f"""PRODUCT INFO;
        Product ID: {self.product_id}
        Product Name: {self.product_name}
        Product Purchase Price: {self.product_purchase_price}
        Product Sale Price: {self.product_sale_price}
        Margin: {self.margin}
        Remarks: {self.remarks}""")

    def set_remarks(self):
        if self.margin < 0:
            self.remarks = "Loss"
        elif self.margin > 0:
            self.remarks = "Profit"
        else:
            self.remarks = None
        return self.remarks

    def set_details():
        ### same problem with the others
        ### you try to create new variable instead of using the class variables which you have already been created with initial
        a = input("Product ID: ")
        b = input("Product Name: ")
        c = float(input("Product Purchase Price: "))
        d = float(input("Product Sale Price: "))
        new_product = Product(a, b, c, d)
        return new_product.set_remarks()

    def get_details():
        ### the same problem here. Actuaally, we don't need to create and to call a list for this problem.
        for i in Product.product_list:
            print (i)

product1 = Product("ABC12", "shirt", 75, 100)
product2 = Product("XYZ15", "soup", 170, 150)
# print(product1.__dict__)
# product1.display_product()

# deneme1 = Product.set_details()
# print(deneme1)
# deneme1.display_product()

# Product.get_details()

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