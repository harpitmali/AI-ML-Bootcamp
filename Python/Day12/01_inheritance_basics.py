class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def meow(self):
        print(f"{self.name} says Moew!")

dog = Dog("Mushu")
cat = Cat("kitty")

dog.eat()
dog.bark()

print()

cat.eat()
cat.meow()