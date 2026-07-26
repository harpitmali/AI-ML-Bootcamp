# Experiment 1 — Your First Class ⭐

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

student1 = Student("Harpit", 21, "AI/ML")
student2 = Student("Luffy", 22, "Web Developer")

print("Student1\n")
print(f"Name: {student1.name}")
print(f"age: {student1.age}")
print(f"Course: {student1.course}")

print()

print("Student2\n")
print(f"Name: {student2.name}")
print(f"Age: {student2.age}")
print(f"Course: {student2.course}")

# Experiment 2 — Methods

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print("Hi!")
        print(f"My name is {self.name}")
        print(f"I am {self.age} years old")
        print(f"My course is {self.course}")

student1 = Student("Harpit", 21, "AI/ML")
student2 = Student("Luffy", 22, "Web Developer")

student1.introduce()
print()
student2.introduce()



# Experiment 3 — Car Class

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

car1 = Car("Tata", "Harrier", 2025)
car2 = Car("Tata", "Nexon", 2024)
car3 = Car("Tata", "Sierra", 2026)

car1.display_info()
print()
car2.display_info()
print()
car3.display_info()


# Experiment 4 — Modify Attributes

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Harpit", 22)
student2 = Student("Dhiraj", 20)

print("Before Updating")
print(f"Name: {student1.name}")
print(f"age: {student1.age}")

print()

print(f"Name: {student2.name}")
print(f"age: {student2.age}\n")

student1.age = 21

print("After Updating")
print(f"Name: {student1.name}")
print(f"age: {student1.age}")

print()

print(f"Name: {student2.name}")
print(f"age: {student2.age}")



# Experiment 5 — Bank Account ⭐⭐

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid Amount")
            return 
        self.balance += amount
        print(f"Deposited: ${amount}")
        print(f"New Balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid Amount")
            return
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawn: ${amount}")
            print(f"Remaining: ${self.balance}")
        else:
            print("Insufficient Balance")

client1 = BankAccount("Harpit", 2500)

client1.deposit(300)
print()
client1.withdraw(2000)
print()
client1.withdraw(1000)