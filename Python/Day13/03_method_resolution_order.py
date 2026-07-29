class Father:
    def greet(self):
        print("Hello from Father")

class Mother:
    def greet(self):
        print("Heloo from Mother")

class Child(Father, Mother):
    pass

child = Child()

child.greet()

print("\nMethod Resolution Order:")
for cls in Child.mro():
    print(cls.__name__)

