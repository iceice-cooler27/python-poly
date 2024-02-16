class Bank:
    def __init__(self, name, account_name, balance):
        self.name = name
        self.account_name = account_name
        self.balance = balance
    def depositMoney(self, amount):
        self.balance += amount
    def withdrawMoney(self, amount):
        self.balance -= amount
    def checkBalance(self):
        print(self.balance)

person = Bank("Adam", 123, 100)
person.checkBalance()
person.depositMoney(50)
person.checkBalance()
person.withdrawMoney(50)
person.checkBalance()