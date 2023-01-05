class ItemInfo:

    def __init__(self):
        pass


    def buy(self):
        self.item_code = input("Enter Item Code: ")
        self.item = input("Enter Item name: ")
        self.item_price = float(input("Enter Price of Item: "))
        self.item_qty = int(input("Enter Quantity in stock: "))

    def calculate_discount(self):
        if self.item_qty <= 10:
            self.item_discount = 0
        elif 11 <= self.item_qty < 20:
            self.item_discount = 15
        else:
            self.item_discount = 20

        self.item_net_price = (self.item_price * self.item_qty) - self.item_discount

        return self.item_net_price

    def show_all(self):
        print(f"İtem code {self.item_code}"
              f"item name {self.item}",
              f"item price {self.item_price}",
              f"item qty {self.item_qty}",
              f"item discount{self.item_discount}",
              f"item netprice{self.item_net_price}")


ItemInfo().buy()
ItemInfo().calculate_discount()
ItemInfo().show_all()




