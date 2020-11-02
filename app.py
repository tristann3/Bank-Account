from random import randint

class BankAccount:
    account_number = randint(0,99999999)
    routing_number = 123456789
    balance = 0

    def __init__(self, full_name):
        self.full_name = full_name
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Amount Deposited: {amount}")
        return
    def withdraw(self, amount):
        self.balance = self.balance - amount
        if self.balance < 0:
            print("Insufficient funds.")
            self.balance = self.balance + amount - 10 #adds withdraw back to account and adds a 10 dollar overdraft fee
            return
        print(f"Amount Withdrawn: {amount}")
        return



my_account = BankAccount("Tristan")
my_account.deposit(100)
my_account.withdraw(110)

print(my_account.balance)
