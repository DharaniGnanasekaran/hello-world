
class BalanceError(Exception):
    value = " No required fund. $%6.2f "


class BankAccount:
    def __init__(self, initialAmount):
        self.balance = initialAmount
        print "Account created . Balance %5.2f" % self.balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
        else:
            raise BalanceError, BalanceError.value % self.balance

    def checkBalance(self):
        return self.balance

    def transfer(self, amount, account):
        try:
            self.withdraw(amount)
            account.deposit(amount)
        except BalanceError:
            print BalanceError.value % self.balance


a = BankAccount(500)
b = BankAccount(200)
#a.withdraw(100)
a.withdraw(1000)
a.transfer(100,b)
print "A = ", a.checkBalance()
print "B = ", b.checkBalance()
