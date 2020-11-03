from random import randint

class BankAccount:
    account_number = randint(0,99999999)
    routing_number = 123456789
    balance = 0

    def __init__(self, full_name):
        self.full_name = full_name
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"\nAmount Deposited: {round(amount, 2)}")
        return
    def withdraw(self, amount):
        self.balance = self.balance - amount
        if self.balance < 0:
            print("\nInsufficient funds. You have been charged an overdraft fee")
            self.balance = self.balance + amount - 10 #adds withdraw back to account and adds a 10 dollar overdraft fee
            return
        print(f"\nAmount Withdrawn: {round(amount, 2)}")
        return
    def get_balance(self):
        print(f"\nYou currently have ${round(self.balance, 2)}")
        return self.balance
    def add_interest(self):
        interest = self.balance *  0.00083
        self.balance = self.balance + interest
        return
    def print_receipt(self):
        print(f"\n{self.full_name}\nAccount No.: {self.account_number} \nRouting No.: {self.routing_number}\nBalance: ${round(self.balance, 2)}")



tristan_account = BankAccount("Tristan Thompson")
elon_account = BankAccount("Elon Musk")
joi_account = BankAccount("Joi Anderson")

tristan_account.deposit(100)
tristan_account.print_receipt()
tristan_account.add_interest()
tristan_account.print_receipt()
tristan_account.withdraw(1000)
tristan_account.print_receipt()


