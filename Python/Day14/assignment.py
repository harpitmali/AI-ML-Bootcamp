# Assignment 1 — Employee Management System ⭐

class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def get_name(self):
        print(f"Name: {self.__name}")

    def get_salary(self):
        print(f"Salary: ₹{self.__salary}")

    def increase_salary(self, amount):
        if amount > 0:
            self.__salary += amount
            print("Salary Increased!")
            self.get_salary()
        else:
            print("Invalid Amount")
        
emp1 = Employee("Harpit", 50000)

emp1.get_name()
print()
emp1.get_salary()
print()
emp1.increase_salary(5000)


# Assignment 2 — Shape Calculator ⭐⭐

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
        print(f"Area: {self.l * self.b}\n")

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        print(f"Area: {3.14 * self.r ** 2}\n")

class Triangle(Shape):
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def area(self):
        print(f"Area: {0.5 * self.h * self.b}\n")

rec = Rectangle(2, 4)
cir = Circle(2)
tri = Triangle(3, 4)

rec.area()
cir.area()
tri.area()

# Assignment 3 — Animal Zoo ⭐⭐⭐

class Lion:
    def make_sound(self):
        print("Roar!\n")

class Elephant:
    def make_sound(self):
        print("Trumpet!\n")

class Monkey:
    def make_sound(self):
        print("Oo Oo Aa Aa!\n")

class Snake:
    def make_sound(self):
        print("Hiss!\n")

animals = [Lion(), Elephant(), Monkey(), Snake()]

for animal in animals:
    animal.make_sound()


# Assignment 4 — Library Book ⭐⭐⭐⭐

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Book({self.title} by {self.author})"
    
    def __len__(self):
        return self.pages
    
    def __eq__(self, other):
        return self.pages == other.pages
    

book1 = Book("Basic of Python", "Harpit", 200)
book2 = Book("Basic of AI/ML", "Luffy", 300)

print(book1)

print(len(book2))

print(book1 == book2)

# Assignment 5 — Authentication Decorator ⭐⭐⭐⭐⭐

logged_in = True

def login_required(func):
    def wrapper():
        if logged_in:
            func()
        else:
            print("Access Denied!")
            print("Please Login.")
    return wrapper

@login_required
def view_profile():
    print("Profile Opened")

view_profile()



# 🌟 Bonus Assignment ⭐⭐⭐⭐⭐

class Wallet:
    def __init__(self, balance):
        self.balance = balance

    def __add__(self, other):
        return self.balance + other.balance
    
wallet1 = Wallet(500)
wallet2 = Wallet(300)

wallet3 = wallet1 + wallet2

print(wallet3)