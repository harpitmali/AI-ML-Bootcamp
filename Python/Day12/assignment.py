# ⭐ Assignment 1 — Person & Student

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
    
class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course
    
    def display_info(self):
        super().display_info()
        print(f"Course: {self.course}")

student1 = Student("Harpit", 21, "AI/ML")
student2 = Student("Dhiraj", 20, "Cyber Security")

student1.display_info()
print()
student2.display_info()

# ⭐⭐ Assignment 2 — Employee & Manager

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_salary(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_salary(self):
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")

manager1 = Manager("Harpit", 50000, "AI/ML")
manager2 = Manager("Luffy", 60000, "Data Science")

manager1.display_salary()
print()
manager2.display_salary()


# ⭐⭐⭐ Assignment 3 — Vehicle Hierarchy

class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def start_engine(self):
        print("Engine Started")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def start_engine(self):
        print("Car Engine Started")

car = Car("Tata", "Harrier")


print(f"Brand: {car.brand}")
print(f"Model: {car.model}")
car.start_engine()


# ⭐⭐⭐⭐ Assignment 4 — Animal Sounds

class Animal:
    def make_sound(self):
        print("Animal Sound")

class Dog(Animal):
    def make_sound(self):
        print("WOOF!")

class Cat(Animal):
    def make_sound(self):
        print("MEOW!")

class Cow(Animal):
    def make_sound(self):
        print("MOO!")

dog = Dog()
cat = Cat()
cow = Cow()

dog.make_sound()
print()
cat.make_sound()
print()
cow.make_sound()


# ⭐⭐⭐⭐⭐ Assignment 5 — Online Shopping System

class Product:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

    def display_product(self):
        print(f"Product Name: {self.product_name}")
        print(f"Price: {self.price}")

class ElectronicProduct(Product):
    def __init__(self, product_name, price, warranty_years):
        super().__init__(product_name, price)
        self.warranty_years = warranty_years

    def display_product(self):
        super().display_product()
        print(f"Warranty Years: {self.warranty_years}")

electronic_product1 = ElectronicProduct("TV", 10000, 2)
electronic_product2 = ElectronicProduct("Laptop", 75000, 3)
electronic_product3 = ElectronicProduct("Fridge", 8000, 2)

electronic_product1.display_product()
print()
electronic_product2.display_product()
print()
electronic_product3.display_product()