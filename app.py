from random import randint

class BankAccount:
    account_number = randint(0,99999999)
    routing_number = 123456789
    balance = 0

    def __init__(self, full_name):
        self.full_name = full_name



my_account = BankAccount("Tristan")
print(my_account.balance)
