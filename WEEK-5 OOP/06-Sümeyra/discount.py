#Define a class named ``ItemInfo` with the following description:
#item_code(Item Code), item(item name), price(Price of each item), qty(quantity in stock)discount(Discount percentage on the item), net_price(Price after discount)

#Methods :
#A member method calculate_discount() to calculate discount as per the following rules:
#If qty <= 10 —> discount is 0
#If qty (11 to 20 inclusive) —> discount is 15
#If qty >= 20 —> discount is 20
#A constructor init method to assign the initial values for item_code to 0 and price, qty, net_price and discount to null
#A function called buy() to allow user to enter values for item_code, item, price, qty. 
#Then call function calculate_discount() to calculate the discount and net_price(price * qty - discount).
#A function show_all() or similar name to allow user to view the content of all the data members.




class Iteminfo:
    def __init__(self,item_code = 0,item = None,price = 0,qty = 0):
          self.item_code = int(item_code)
          self.item = item
          self.price = float(price)
          self.qty = int(qty)

    def input_data(self):
        self.item_code = int(input("What is the code of the product you want to buy? :"))
        self.item = input("What is the name of the product you want to buy? :")
        self.price = float(input("What is the price of the product you want to buy? :")) 
        self.qty = int(input("What is the stock amount of the product you want to buy? :"))      

    def calculate_discount(self): 
          if self.qty <= 10:
            return 0
          elif 11 <= self.qty < 20:
            return int(self.qty) * int(self.price)*15/100
          else:
            return int(self.qty) * int(self.price)*20/100
      
    def buy(self):
        return int(self.qty) * int(self.price) - int(self.calculate_discount()) 

    def show_all(self):
        print(f"\nItem_code : {self.item_code}\nItem name : {self.item}",
              f"\nPrice : {self.price}\nQuantity : {self.qty}",
              f"\nDiscount amount : {self.calculate_discount()}"
              f"\nNet price : {self.buy()}") 

product = Iteminfo()
product.input_data()

print(product.show_all())      
      

              

