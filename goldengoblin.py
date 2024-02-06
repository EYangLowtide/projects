class BankAccount:
    # Class attribute
    bank_title = "Golden Goblin"  # Placeholder name, can be set to the actual bank title
    
    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.current_balance += amount
            print(f"{self.customer_name} you have deposited {amount}. Your new balance is: {self.current_balance}")
        else:
            print("Deposit amount must be a positive number.")
    
    def withdraw(self, amount):
        if amount > 0 and self.current_balance - amount >= self.minimum_balance:
            self.current_balance -= amount
            print(f"{self.customer_name} you have withdrawn {amount}. Your new balance is: {self.current_balance}")
        else:
            print("Insufficient funds for withdrawal or minimum balance requirement not met.")
    
    def print_customer_information(self):
        print(f"Bank: {BankAccount.bank_title}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Current Balance: {self.current_balance}")
        print(f"Minimum Balance: {self.minimum_balance}")

#two different instances
account1 = BankAccount("Clark Kent", 1000, 100)
account1.print_customer_information() # Print customer information
account1.deposit(500) # Test deposits
account1.withdraw(200) # Test withdrawals
account1.print_customer_information() # Print customer information to see changes

account2 = BankAccount("Bruce Wayne", 500, 50)
account2.print_customer_information() # Print customer information
account2.deposit(200) # Test deposits
account2.withdraw(100) # Test withdrawals
account2.print_customer_information() # Print customer information to see changes
