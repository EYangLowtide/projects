### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""

### Make an instance of SandwichMachine class and write the rest of the codes ###

class SandwichMachine:
    def __init__(self, machine_resources):
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        for ingredient, amount_required in ingredients.items():
            if self.machine_resources[ingredient] < amount_required:
                print(f"Sorry there is not enough {ingredient}.")
                return False
        return True

    def process_coins(self):
        total = 0
        total += int(input("how many large dollars?: ")) * 1
        total += int(input("how many half dollars?: ")) * 0.5
        total += int(input("how many quarters?: ")) * 0.25
        total += int(input("how many nickels?: ")) * 0.05
        return total

    def transaction_result(self, coins, cost):
        if coins < cost:
            print("Sorry, that's not enough money. Money refunded.")
            return False
        elif coins > cost:
            print(f"Here is ${coins - cost:.2f} in change.")
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        for ingredient, amount in order_ingredients.items():
            self.machine_resources[ingredient] -= amount
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")

def main():
    machine = SandwichMachine(resources)
    while True:
        choice = input("What would you like? (small/ medium/ large/ off/ report): ").lower()
        if choice == "off":
            break
        elif choice == "report":
            for resource, amount in machine.machine_resources.items():
                print(f"{resource.title()}: {amount} slice(s)" if resource == "bread" else f"{resource.title()}: {amount} ounce(s)")
        elif choice in recipes:
            if machine.check_resources(recipes[choice]["ingredients"]):
                print("Please insert coins.")
                coins = machine.process_coins()
                if machine.transaction_result(coins, recipes[choice]["cost"]):
                    machine.make_sandwich(choice, recipes[choice]["ingredients"])
        else:
            print("Invalid selection. Please choose again.")

if __name__ == "__main__":
    main()
