class Encapsulation:
    def public(self):
        """accessible by object of the class as well as by other inheriting class"""
        print("Public Method")

    def _protected(self):
        """Intended to be accessed only within the class and its subclasses."""
        print("Protected Method")

    def __private(self):
        """Cannot be accessed directly from outside the class."""
        print("Private Method")

    def use_private(self):
        self.__private()

obj = Encapsulation()
obj.public()
obj._protected()
#obj.__private() - throws error
obj.use_private()

"""
Problem Statement:
Create a class BankAccount with:

A private attribute __balance initialized to 0

Public methods:

deposit(amount)

withdraw(amount)

get_balance() (returns balance)

Make sure negative balances aren’t allowed.

Expected Output:

acc = BankAccount()
acc.deposit(1000)
print(acc.get_balance())    # 1000
acc.withdraw(500)
print(acc.get_balance())    # 500
acc.withdraw(1000)          # Insufficient balance

Deposited: 1000
Balance: 1000
Withdrew: 500
Balance: 500
Insufficient balance!
"""

class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited: ", amount)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrew: ", amount)
        else:
            print("Insufficient balance!")

    def get_balance(self):
        print("Balance: ", self.__balance)


acc = BankAccount()
acc.deposit(1000)
acc.get_balance()
acc.withdraw(500)
acc.get_balance()
acc.withdraw(1000)
