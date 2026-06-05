from abc import ABC , abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        print("Dog Bark")

d = Dog()
d.sound()

# Abstraction class and method

from abc import ABC , abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    def sleep(self):
        print("Animal is sleeping")

class Dog(Animal):

    def sound(self):
        print("Dog Bark")

class Cat(Animal):

    def sound(self):
        print("Cat meow")

d = Dog()
c = Cat()
c.sound()
c.sleep()
d.sound()
d.sleep()
