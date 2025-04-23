"""
By default, function overloading is not possible in python
Example -

def add(a, b, c):
    return a + b + c

def add(a, b):
    return a + b

print(add(1, 2, 3)) this gives TypeError: add() takes 2 positional arguments but 3 were given
"""
# In order to implement this , we use default args
def add(a, b, c=0):
    return a + b + c
print(add(1, 2, 3))
print(add(1, 2))