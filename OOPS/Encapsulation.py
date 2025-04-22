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
