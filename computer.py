 # What attributes will it need?
#ability to create computer and create identifying features
#ability to update the features (price and system as definied by ReadMe)

    # How will you set up your constructor?
#constructs computer item with variables set by procedural resale shop file
    # Remember: in python, all constructors have the same name (__init__)
    
    # What methods will you need?
#basic method to create computer item
#update_price
#update_OS system

#identifies computer item
class Computer:  
    """A class representing a computer."""

    def __init__(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price):
        """Initialize a computer with its attributes."""
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    def update_price(self, new_price):
        """Update the price of the computer."""
        self.price = new_price

    def update_os(self, new_os):
        """Update the operating system of the computer."""
        self.operating_system = new_os
