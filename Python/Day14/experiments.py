# Experiment 1 — Polymorphism

class Dog:
    def speak(self):
        print("Dog Says: WOOF!")

class Cat:
    def speak(self):
        print("Cat Says: MEOW!")

class Cow:
    def speak(self):
        print("Cow Says: MOO!")

animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.speak()


# Experiment 2 — Duck Typing
    
class Bike:
    def start(self):
        print("Bike Started...")

class Car:
    def start(self):
        print("Car Started...")

def start_vehicle(vehicle):
    vehicle.start()

start_vehicle(Bike())
start_vehicle(Car())
# Experiment 3 — Encapsulation

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
        

    def get_balance(self):
        print(f"Balance: {self.__balance}")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit: {amount}")
            print(f"Balance: {self.__balance}")
        else:
            print("Invalid Input")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid Amount")
        if amount > self.__balance:
            print("Not Enough Balance")
        else:
            self.__balance -= amount
            print(f"Withdraw: {amount}")
            self.get_balance()

bankAccount1 = BankAccount(0)

bankAccount1.get_balance()

bankAccount1.deposit(500)

bankAccount1.withdraw(300)


# Experiment 4 - Abstraction

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        print(f"Area: {self.l * self.b}")

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        print(f"Area: {3.14 * self.r ** 2}")

rec = Rectangle(3, 4)

cir = Circle(2)

rec.area()
print()
cir.area()


# Experiment 5 — Magic Methods

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Student(Name={self.name}, Marks={self.marks})"
    
    def __eq__(self, other):
        return self.marks == other.marks

    
student1 = Student("Harpit", 97)

print(student1)

student2 = Student("Luffy", 97)

print(student1==student2)


# Experiment 6 — Decorators

def logger(func):
    def wrapper():
        print("Starting Function...\n")

        func()

        print("\nFunction Executed")
        print("Ending Function...")
    return wrapper


@logger
def study():
    print("Studying Python...")


study()

# Bonus 

class ShoppingCart:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)
    
cart = ShoppingCart(["Laptop", "Mouse", "Keyboard"])

print(len(cart))