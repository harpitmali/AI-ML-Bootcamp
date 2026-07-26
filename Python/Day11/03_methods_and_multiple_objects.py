class Dog:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}")

    def bark(self):
        print(f"{self.name} says Woof!")

dog1 = Dog("Bruno")
dog2 = Dog("Ronney")

dog1.introduce()
dog1.bark()

print()

dog2.introduce()
dog2.bark()