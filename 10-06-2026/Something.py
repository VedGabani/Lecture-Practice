'''

Remaining OOP Topic

Two Type

1. Method overloading
2. Method overriding

1) Method overloading means creating multiple method
with same name diff parameter

'''

class Calculator:

    def add(self , a , b = 0 , c = 0):
        return a + b +c

obj = Calculator()
print(obj.add(10 , 20))
print(obj.add(10 , 20 , 30))

'''

2) Method overriding

It occurs when child class provide a diff implimentation
of a method already define in thw parent class

'''

class Animal:

    def sound(self):
        print("Animal make sound")

class Dog(Animal):

    def sound(self):
        print("Dog make sound")

obj = Dog()
obj.sound()

'''

issubclass is built in Python fn used to check weather
one class is a subclass of another class

'''

class Animal():
    pass

class Dog(Animal):
    pass

print(issubclass(Dog , Animal))
print(issubclass(Animal , Dog))

'''

Super class is used to class method or constructor
of the parent class frpm the child class

'''

class Person:

    def __init__(self , name):
        self.name = name

class Student(Person):

    def __init__(self , name , last):
        super().__init__(name)
        self.last = last

    def display(self):

        print("Name -_- ", self.name)
        print("Surname -_- ", self.last)

obj = Student("Ved" , "Gabani")
obj.display()

# 1. Using super() with constructor

class Parent:

    def __init__(self):
        print("Parent Constructor")

class Child(Parent):

    def __init__(self):

        super().__init__()

        print("Child Constructor")

obj = Child()

# 2. Access parent class method

class Animal:

    def sound(self):
        print("Makes sound")

class Dog(Animal):

    def sound(self):
        super().sound()
        print("Dog Sound")

obj = Dog()
obj.sound()

# 3. Parent class and Child class both have variable

class Person:

    def __init__(self , name):
        self.name = name

class Student(Person):

    def __init__(self , name , last):
        super().__init__(name)
        self.last = last

    def display(self):

        print("Name -_- ", self.name)
        print("Surname -_- ", self.last)

obj = Student("Ved" , "Gabani")
obj.display()
