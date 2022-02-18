from click import option
from numpy import quantile


class Seller:
    def __init__(self):
        self.products_quantity = {}
        self.products_price = {}
        self.profit = 0

    def update(self):
        item_name = input("Enter Name: ")
        item_quantity = int(input("Enter Quantity: "))
        item_price = int(input("Enter Price: "))
        self.products_quantity[item_name] = item_quantity
        self.products_price[item_name] = item_price

    def show(self):
        print("Showing Items...\n")
        for i, j in self.products_quantity.items():
            print(i, j)

    def buy(self, item_name, quantity):
        if quantity > self.products_quantity.get(item_name):
            print("Sorry we dont have that much")
        else:
            self.products_quantity[item_name] = self.products_quantity.get(
                item_name) - quantity
            self.profit += self.products_price.get(item_name)*quantity

class Buyer:
    def __init__(self):
        self.cart = {}
        self.quantity = {}
        self.total_amt = 0

    def search(self, seller, item_name):
        if seller.products_quantity.get(item_name):
            print("Quantity: {}".format(seller.products_quantity.get(item_name)))
            print("Price: {}".format(seller.products_price.get(item_name)))
            choice = input("Do you want to add this to your cart? y/n: ")
            if choice == "y":
                quantity = int(input("Enter quantity: "))
                if quantity > seller.products_quantity.get(item_name):
                    print("We do not have that much!")
                    self.search(seller, item_name)

                else:
                    self.cart[item_name] = seller.products_price.get(
                        item_name)*quantity
                    self.quantity[item_name] = quantity
                    self.total_amt += seller.products_price.get(
                        item_name)*quantity
            else:
                pass

        else:
            return "No such product exists"

    def show(self):
        print("Showing Items...\n")
        for i, j in self.cart.items():
            print(i, j)

    def buy(self, seller):
        print("There are items in your cart...")
        self.show()
        print("Total payable amount is {}".format(str(self.total_amt)))
        for item, quantity in self.quantity.items():
            seller.buy(item, quantity)


out_option = True
seller = Seller()
buyer = Buyer()
while out_option:
    choice = input("Are you a buyer or a seller? b/s: ")
    if choice == 's':
        option = True
        while option:
            print("1. Update Items")
            print("2. Show Items")
            print("3. Exit\n")
            choice = input("Enter Option: ")
            print("")
            if(choice == '1'):
                seller.update()
            elif(choice == '2'):
                seller.show()
            elif(choice == '3'):
                option = False
            else:
                print('enter a valid number')
    elif choice == 'b':
        option = True
        while option:
            print("1. Search Items")
            print("2. Buy Items")
            print("3. Exit\n")
            choice = input("Enter Option: ")
            print("")
            if(choice == '1'):
                item_name = input("Enter name of product: ")
                buyer.search(seller, item_name)
            elif(choice == '2'):
                buyer.buy(seller)
            elif(choice == '3'):
                option = False
            else:
                print('enter a valid number')
    else:
        out_option = False
        print("Exiting system...")

# option = True
# data = {}
# def update(data):
#     item_name = input("Enter Name: ")
#     item_quantity = input("Enter Quantity: ")
#     print("")
#     data[item_name] = item_quantity
# def show(data):
#     print("Showing Items...\n")
#     for i, j in data.items():
#         print(i, j)
# def search(data, key):
#     return data.get(key)
# while option:
#     print("1. Update Items")
#     print("2. Show Items")
#     print("3. Search Items")
#     print("4. Exit\n")
#     choice = input("Enter Option: ")
#     print("")
#     if(choice == '1'):
#         update(data)
#     elif(choice == '2'):
#         show(data)
#     elif(choice == '3'):
#         key=input("Enter the item to be searched: ")
#         print(search(data,key))
#     elif(choice == '4'):
#         option = False
#     else:
#         print('enter a valid number')

# class Car:
#     def __init__(self, name, engine, torque, type, owner):
#         self.engine = engine
#         self.owner = owner
#         self.name = name
#         self.torque = torque
#         self.type = type


# swift = Car('swift', '1100', '500', 'hatchback', 'Meet')
# fortuner = Car('fortuner', '2200', '1200', 'SUV', 'Meet')
# print("my name is "+ swift.owner + " my car is " + swift.name + " with an engine of " + swift.engine +
#       " cc, and a torque of " + swift.torque + " and a body type of " + swift.type)
# print("my name is "+ fortuner.owner + " my car is " + fortuner.name + " with an engine of " + fortuner.engine +
#       " cc, and a torque of " + fortuner.torque + " and a body type of " + fortuner.type)

# class Mathe:
#     def __init__(self, number, power):
#         self.number = number
#         self.power = power
#     def square(self):
#         return self.number**self.power
# example1 = Mathe(5,3)
# x = example1.square()
# print(x)

# class Utensils:
#     def __init__(self, material, name):
#         self.material = material
#         self.name = 'Utensil'

#     def inspect(self):
#         print("The material of " + self.name + " is: "+self.material)


# tava = Utensils('steel', 'tava')
# tava.inspect()


# class Plate(Utensils):
#     def __init__(self, material, name):
#         Utensils.__init__(self, material, name)
#     def inspect(self):
#         print("The {} is of: {}".format(self.name, self.material))
# class Jar(Utensils):
#     def __init__(self, material, name):
#         super().__init__(material, name)
#         self.name = name
#     def inspect(self):
#         print("The {} is made up of of: {}".format(self.name, self.material))
# dish = Plate("Glass", "Dish")
# dish.inspect()
# Vaccumjar = Jar("Melamine", "VaccumJar")
# Vaccumjar.inspect()