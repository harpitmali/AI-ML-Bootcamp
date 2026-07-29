class Animal:
    def eat(self):
        print("Animal is eating.")

class Dog(Animal):
    def bark(self):
        print("Dog says Woof!")

class Puppy(Dog):
    def cry(self):
        print("Puppy is whining.")

puppy = Puppy()

puppy.eat()
puppy.bark()
puppy.cry()