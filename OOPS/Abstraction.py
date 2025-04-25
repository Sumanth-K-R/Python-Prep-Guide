from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract class

    @abstractmethod
    def sound(self):  # Abstract method
        pass

class Dog(Animal):  # Concrete class
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# animal = Animal()  # Error: Can't instantiate abstract class
dog = Dog()
cat = Cat()

print(dog.sound())  # Bark
print(cat.sound())  # Meow


"""
Problem Statement:
Define an abstract base class PaymentMethod with:

Abstract method make_payment(amount)

Create concrete classes:

CreditCard → prints "Paid ₹<amount> via Credit Card"

PayPal → prints "Paid ₹<amount> via PayPal"

UPI → prints "Paid ₹<amount> via UPI"

Then write a function that accepts any payment object and amount, and processes the payment.

Expected Output:

payments = [CreditCard(), PayPal(), UPI()]

for method in payments:
    method.make_payment(500)

Paid ₹500 via Credit Card
Paid ₹500 via PayPal
Paid ₹500 via UPI
"""

class Payment(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass

class CreditCard(Payment):
    def make_payment(self, amount):
        print(f"Paid {amount} via Credit Card")

class PayPal(Payment):
    def make_payment(self, amount):
        print(f"Paid {amount} via PayPal")

class UPI(Payment):
    def make_payment(self, amount):
        print(f"Paid {amount} via UPI")

def process_payment(payment, amount):
    payment.make_payment(amount)

cc = CreditCard()
pp = PayPal()
upi = UPI()
process_payment(cc, 500)
process_payment(pp, 500)
process_payment(upi, 500)