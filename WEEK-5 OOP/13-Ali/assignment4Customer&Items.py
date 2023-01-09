
class Customer:
    customerID = 0
    Customerorder = 0
    def __init__(self, name=str(),last_name =str(),customer_id = int()):
        Customer.Customerorder += 1 
        self.name = name
        self.last_name = last_name
        self.customer_id= customer_id
        self.get_cust_info()
        Customer.customerID = self.customer_id
        self.__str__()

        
      
        
    def get_cust_info(self):       
        self.name = input("enter please customer name: ")
        self.last_name = input("enter please customer lastname: ")
        self.customer_id = input("enter please customer ID: ")
        pass # to allow customer to enter his/her information or just define them in init and pass customer info as argument while criating a customer object
    def __str__(self):            
        print(f"Customer{Customer.Customerorder}=[name: {self.name} ,lastname: {self.last_name}, customer id: {self.customer_id}]")   
        pass # print customer infor.... find a way to link two classes.

         
        


class Items():
    

    backlog = []
    StorageDict = {}
    ShoppingCartDict2 = {}                           # dict is used to reach other atteributes after all the object have been created 
    quantityToCart = {}                              # in this dict items and their quantities will be accummulated which in shopping cart 
    ShoppingCartOrder = 0
    itemNamen= []

    def __init__(self, item_name, price, qty):
        
        self.item_name = item_name 
        self.total_price = 0
        self.price = price
        self.qty = qty
        self.qtyToCart = 0
        self.price_tobe_paid = 0
        self.discount = 0
        self.item_to_cart = None
        self.AddBacklog()
        self.print3()            # this method bring Product list for helping before user write product name to add Shophing cart
        # self.__str__()
        # self.itemNames()
        # self.shopping_cart()
    

    
    def AddBacklog(self):
        Items.backlog.append([self.item_name, self.price,self.qty])

        Items.StorageDict[self.item_name] = {"price": self.price, "qty": self.qty}
    
    def __str__(self):     #Shopping_cart1 =[customer_id : 123, items : [necklace, ring, ear ring], total_price : 2000, discount : 300, price_tobe_paid : 1700 ]
        print(f"ShoppingCart{Items.ShoppingCartOrder}= [Customer id: {Customer.customerID} ,items: {Items.itemNamen} total price: {self.total_price}, disount: {self.discount}, price tobe paid: {self.price_tobe_paid}]")
    
    def calculate_discount(self):

        if self.total_price >= 400:   # bir 0 eksik yazıldı 
            self.discount = 25
        elif self.total_price >= 200:
            self.discount = 15
        elif self.total_price < 200:
            self.discount = 10
        self.price_tobe_paid = self.total_price - self.discount
        # print(self.price_tobe_paid)
        
    def print3 (self):
        print(f"item name: {self.item_name}")    
        
    
    def shopping_cart(self):
           
        while True:
            try:
                # (self.item_to_cart,self.qty) = (input("enter please item name to add it to the cart or enter x to end item chosing: "),int(input("enter please quantity of item you want to add to chopping cart: ")))
                self.item_to_cart = input("enter item name from list above to add it to the cart or enter \"exit\" to end item chosing: ")
                if self.item_to_cart in Items.StorageDict.keys():                  #customer can write item name from the list exhibited above otherwise he/she take a warnung
                    Items.ShoppingCartDict2[self.item_to_cart] = Items.StorageDict[self.item_to_cart]
                    self.qtyToCart = int(input("enter the quantity of item you want to add: "))      #customer enters quentity here for the item he chosen 2 row above
    
                    Items.quantityToCart[self.item_to_cart] = self.qtyToCart                    
                elif self.item_to_cart == "exit":                                      #this step ends choosing item to shopping cart
                    break                
                elif self.item_to_cart not in Items.StorageDict.keys():     #backlog:
                    raise TypeError
            except TypeError:
                print("enter please accurete name of item")    
        Items.ShoppingCartOrder +=1 
        for i in Items.ShoppingCartDict2.keys():
            Items.itemNamen.append(i)
        

        self.get_total_amount()
        self.calculate_discount()
        self.__str__()
  
    def print(self):
        print(f"item name: {self.item_name}")
        
        
       
    def get_total_amount(self):
        for index in Items.ShoppingCartDict2.keys() :
            self.total_price += (Items.ShoppingCartDict2[index]["price"])*(Items.quantityToCart[index])

customer1 = Customer()


namenSource1 = [    # objects of the Class "Items" will be created from the element of this list       
    ("Jam",240, 134), 
    ("Honey",332,101), 
    ("Peanut butter",196,127), 
    ("Syrup golden, maple",177,200), 
    ("Mustard",180,60), 
    ("Marmite",193,69), 
    ("Ketchup",180,52), 
    ("Cooking wine",250,141), 
    ("Oil olive sunflower",219,86), 
    ("Soy sauce",125,118), 
    ("Salsa",277,55), 
    ("Sriracha",122,117), 
    ("BBQ sauce",199,72), 
    ("Chipotle",173,96), 
    ("Tomato puree",390,128), 
    ("Capers",164,188), 
    ("Olives",239,104), 
    ("Lemon juice",250,139), 
    ("Tikka paste",200,188),     
]
entities = []  
for i in namenSource1:
    newEntity = Items(i[0],i[1],i[2])
    entities.append(newEntity)


entities[0].shopping_cart()