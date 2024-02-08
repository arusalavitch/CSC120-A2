# What attributes will it need?
#name class and import computer
#buy, price, sell, inventory, update, return FALSE when computer not in inventory
    # How will you set up your constructor?
#give initial conditions with empty inventory 
    # Remember: in python, all constructors have the same name (__init__)
  # You'll remove this when you fill out your constructor

    # What methods will you need?
#buy, price, sell, inventory, update, return FALSE when computer not in inventory

import computer
#make resale shop
class ResaleShop:
    def __init__(self):
        self.inventory = {}
        self.item_id = 0
#create a function to buy computer
    def buy(self, computer):
        self.item_id += 1
        self.inventory[self.item_id] = computer
        return self.item_id
#create function to update price of computer
    def update_price(self, item_id, new_price):
        if item_id in self.inventory:
            self.inventory[item_id].update_price(new_price)
        else:
            print("Item", item_id, "not found. Cannot update price.")
#sell computer
    def sell(self, item_id):
        if item_id in self.inventory:
            del self.inventory[item_id]
            print("Item", item_id, "sold!")
        else:
            print("Item", item_id, "not found. Please select another item to sell.")
#return inventory
    def print_inventory(self):
        if self.inventory:
            for item_id, computer in self.inventory.items():
                print(f'Item ID: {item_id} : {computer.__dict__}')
        else:
            print("No inventory to display.")
#update computer with new information
    def refurbish(self, item_id, new_os=None):
        if item_id in self.inventory:
            computer = self.inventory[item_id]
            if computer.year_made < 2000:
                computer.update_price(0)
            elif computer.year_made < 2012:
                computer.update_price(250)
            elif computer.year_made < 2018:
                computer.update_price(550)
            else:
                computer.update_price(1000)
#indicate when the computer isn't in inventory
            if new_os is not None:
                computer.update_os(new_os)
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")

