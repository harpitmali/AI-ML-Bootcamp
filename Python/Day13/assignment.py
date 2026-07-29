# ⭐ Assignment 1 — Multiple Inheritance

class Singer:
    def sing(self):
        print("Singing...")

class Dancer:
    def dance(self):
        print("Dancing...")

class Performer(Singer, Dancer):
    def perform(self):
        print("Performing on the stage...")


performer = Performer()
performer.sing()
performer.dance()
performer.perform()

# ⭐⭐ Assignment 2 — Multilevel Inheritance

class Device:
    def power_on(self):
        print("Device Powered On")

class Computer(Device):
    def boot(self):
        print("Computer Booting...")

class Laptop(Computer):
    def code(self):
        print("Coding in Python...")

laptop = Laptop()

laptop.power_on()
laptop.boot()
laptop.code()

# ⭐⭐⭐ Assignment 3 — MRO

class A:
    def show(self):
        print("A")

class B:
    def show(self):
        print("B")

class C(A, B):
    def test(self):
        self.show
        print(C.mro())

c = C()
c.test()

# ⭐⭐⭐⭐ Assignment 4 — Multiple Inheritance with Constructors

class Person:
    def __init__(self, name):
        self.name = name
        print("Person Constructor")
    
class Employee:
    def __init__(self, company):
        self.company = company
        print("Employee Constructor")

class Developer(Person, Employee):
    def __init__(self, name, company, language):
        super().__init__(name)
        Employee.__init__(self, company)
        self.language = language

    def display(self):
        print(f"Name: {self.name}")
        print(f"Company: {self.company}")
        print(f"language: {self.language}")

dev1 = Developer("Harpit", "OpenAI", "Python")

dev1.display()


# ⭐⭐⭐⭐⭐ Assignment 5 — School Hierarchy

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_teacher(self):
        super().display_info()
        print(f"Subject: {self.subject}")

class MathsTeacher(Teacher):
    def __init__(self, name, age, subject, experience):
        super().__init__(name, age, subject)
        self.experience = experience

    def display_all(self):
        super().display_teacher()
        print(f"Experience(years): {self.experience}")

mathsTeacher = MathsTeacher("Harpit", 21, "Maths", 3)

mathsTeacher.display_all()

