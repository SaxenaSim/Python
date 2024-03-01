class BankAccount:
    def __init__(self,initial_deposit):
        self.balance=initial_deposit

    def print_balance(self):
        print("balance:",self.balance)

    def __add__(self,other):
        total = self.balance + other.balance
        return BankAccount(total)
    
account1=BankAccount(1000)
account2=BankAccount(2000)
new_Account = account1+account2
new_Account.print_balance()

# it defines how will be the objects of a class added together.