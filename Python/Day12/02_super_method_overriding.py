class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def sound(self):
        print(f"{self.name} says Meow!")


dog = Dog("Mushu", "Husky")
cat = Cat("Kitty")

print(dog.name)
print(dog.breed)

print()
dog.sound()
cat.sound()