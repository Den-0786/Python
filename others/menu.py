class MenuItem:
        """Models for the menu items"""
        def __init__(self, name, water, milk, coffee, cost):
            self.name = name
            self.cost = cost
            self.ingredients = {
                "water": water,
                "milk": milk,
                "coffee": coffee
            }
class Menu:
    """models the menu with 3 menu items"""
    def __init__(self):
        self.menu = [
            MenuItem(name= "latte", water="200", milk="150", coffee="24", cost="2.5"),
            MenuItem(name= "espresso", water="50", milk="0", coffee="18", cost="1.5"),
            MenuItem(name= "cappuccino", water="250", milk="50", coffee="24", cost="3"),
        ]
        
    def get_items(self):
        """Returns a list of all items in the menu"""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
            return options
        
    def find_drink(self, order_name):
        """Search the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available")