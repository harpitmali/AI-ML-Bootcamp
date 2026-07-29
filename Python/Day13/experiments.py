# ⭐ Experiment 1 — Multiple Inheritance

class Teacher:
    def teach(self):
        print("Teacher is teaching")

class Artist:
    def draw(self):
        print("Artist is drawing")

class Student(Teacher, Artist):
    pass

student = Student()
student.teach()
print()
student.draw()

# ⭐⭐ Experiment 2 — Multilevel Inheritance

class LivingThings:
    def live(self):
        print("That is LivingThings")

class Animal(LivingThings):
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Woof!")

dog = Dog()
dog.live()
dog.eat()
dog.bark()

# ⭐⭐⭐ Experiment 3 — MRO

class A:
    def display(self):
        print("A")

class B:
    def display(self):
        print("B")

class C(A, B):
    pass

C().display()
print(C.mro())


# ⭐⭐⭐⭐ Experiment 4 — Constructor + MRO

class Parent1:
    def __init__(self):
        print("Hello from Parent1")

class Parent2:
    def __init__(self):
        print("Hello from Parent2")

class Child(Parent1, Parent2):
    pass

child = Child()