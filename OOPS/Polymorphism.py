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

"""
Problem Statement:
Create a base class Animal with a method make_sound().

Then create subclasses:

Lion → make_sound() prints "Roar!"

Elephant → make_sound() prints "Trumpet!"

Monkey → make_sound() prints "Chatter!"

Write a function animal_sound(animal) that takes any animal object and calls make_sound().

Expected Output:

animals = [Lion(), Elephant(), Monkey()]

for animal in animals:
    animal_sound(animal)

Roar!
Trumpet!
Chatter!    
"""

class Animal:
    def make_sound(self):
        pass

class Lion(Animal):
    def make_sound(self):
        print("Roar!")

class Elephant(Animal):
    def make_sound(self):
        print("Trumpet!")

class Monkey(Animal):
    def make_sound(self):
        print("Chatter!")

lion = Lion()
elephant = Elephant()
monkey = Monkey()
lion.make_sound()
elephant.make_sound()
monkey.make_sound()