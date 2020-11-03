from random import randint

class BankAccount:
    account_number = randint(0,99999999)
    routing_number = 123456789
    balance = 0

    def __init__(self, full_name):
        self.full_name = full_name
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Amount Deposited: {round(amount, 2)}")
        return
    def withdraw(self, amount):
        self.balance = self.balance - amount
        if self.balance < 0:
            print("Insufficient funds.")
            self.balance = self.balance + amount - 10 #adds withdraw back to account and adds a 10 dollar overdraft fee
            return
        print(f"Amount Withdrawn: {round(amount, 2)}")
        return
    def get_balance(self):
        print(f"You currently have ${round(self.balance, 2)}")
        return self.balance
    def add_interest(self):
        interest = self.balance *  0.00083
        self.balance = self.balance + interest
        return
    def print_receipt(self):
        print(f"{self.full_name}\nAccount No.: {self.account_number} \nRouting No.: {self.routing_number}\nBalance: ${round(self.balance, 2)}")



my_account = BankAccount("Tristan")
my_account.deposit(100)
my_account.add_interest()
print(my_account.get_balance())
my_account.print_receipt()

