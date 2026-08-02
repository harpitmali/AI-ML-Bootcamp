class Dog:
    def speak(self):
        print("WOOF!")

class Cat:
    def speak(self):
        print("MEOW!")

animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()


# Build-in Polymorphism
    
print(len("Harpit"))
print(len([1, 2, 3]))
print(len({"a":1, "b":2}))