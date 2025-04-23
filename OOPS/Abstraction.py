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
