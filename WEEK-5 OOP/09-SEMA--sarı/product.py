
class Product:

    def __init__(self):
        pass



    def SetRemarks(self):

        self.Margin = (self.product_sale_price) - (self.product_purchase_price)

        if self.Margin < 0:
            return "Loss"
        elif self.Margin > 0:
            return "Profit"


    def set_details(self):
        self.product_id=input("please enter your product id:")
        self.product_name=input("Please enter your product name:")
        self.product_purchase_price=float(input("Please enter product purchase price:"))
        self.product_sale_price=float(input("Please enter sale price:"))
        self.SetRemarks()


    def get_details(self):
        print(f"Product_id : {self.product_id}\n Product_name :{self.product_name}\nProduct_sale_price: {self.product_sale_price} ")



product_1=Product()
product_1.set_details()
product_1.get_details()