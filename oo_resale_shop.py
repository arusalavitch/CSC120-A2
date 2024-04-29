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

class ResaleShop:
    """A class representing a resale shop for computers."""

    def __init__(self):
        """Initialize the ResaleShop with an empty inventory."""
        self.inventory = {}
        self.item_id = 0

    def buy(self, computer):
        """Add a computer to the inventory."""
        self.item_id += 1
        self.inventory[self.item_id] = computer
        return self.item_id

    def update_price(self, item_id, new_price):
        """Update the price of a computer."""
        if item_id in self.inventory:
            self.inventory[item_id].update_price(new_price)
        else:
            print("Item", item_id, "not found. Cannot update price.")

    def sell(self, item_id):
        """Sell a computer from the inventory."""
        if item_id in self.inventory:
            del self.inventory[item_id]
            print("Item", item_id, "sold!")
        else:
            print("Item", item_id, "not found. Please select another item to sell.")

    def print_inventory(self):
        """Print the inventory."""
        if self.inventory:
            for item_id, computer in self.inventory.items():
                print(f'Item ID: {item_id} : {computer.__dict__}')
        else:
            print("No inventory to display.")

    def refurbish(self, item_id, new_os=None):
        """Refurbish a computer in the inventory."""
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

            if new_os is not None:
                computer.update_os(new_os)
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")
