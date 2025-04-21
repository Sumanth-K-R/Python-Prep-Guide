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

