class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }

    def report(self):
        """Print report of all resources"""
        print(f"water:{self.resources['water']}ml")
        print(f"milk:{self.resources['milk']}ml")
        print(f"coffee:{self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """Returns True if coffee can be made, otherwise false if it can't be made"""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"sorry, there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources"""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} . Enjoy")
