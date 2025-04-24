"""Sample Inheritance Demonstration"""
# Single Inheritance

class A:
    def __init__(self):
        print("Parent Class")

class B(A):
    def __init__(self):
        super().__init__()
        print("Child Class")

obj = B()

# Multiple Inheritance

class C:
    def __init__(self):
        print("Parent Class 1")

class D:
    def __init__(self):
        print("Parent Class 2")

class E(C, D):
    def __init__(self):
        super().__init__() # According to MRO (Method Resolution Order) first Parent class wil be picked
        D.__init__(self)
        print("Child Class of C and D")

obj2 = E()


#---------------------------------------------------------------------------------------------------------------------



"""
Problem Statement:
Design a class hierarchy for a system that manages users of an application. There is a base class called User that contains:

Attributes: username, email

Method: display_info()

Create two subclasses:

Admin with an additional method view_dashboard() that prints "Admin Dashboard Accessed"

Customer with an additional method view_products() that prints "Product List Viewed"

admin = Admin("admin_user", "admin@example.com")
customer = Customer("cust_user", "customer@example.com")

admin.display_info()        # Username: admin_user, Email: admin@example.com
admin.view_dashboard()      # Admin Dashboard Accessed

customer.display_info()     # Username: cust_user, Email: customer@example.com
customer.view_products()    # Product List Viewed

"""

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

class Admin(User):
    def __init__(self, username, email):
        super().__init__(username, email)

    def display_info(self):
        print(self.username, self.email)

    def view_dashboard(self):
        print("Admin Dashboard Accessed")

class Customer(User):
    def __init__(self, username, email):
        super().__init__(username, email)

    def view_products(self):
        print("Product List Viewed")

    def display_info(self):
        print(self.username, self.email)

admin = Admin("admin_user", "admin@example.com")
customer = Customer("cust_user", "customer@example.com")

admin.display_info()
admin.view_dashboard()

customer.display_info()
customer.view_products()