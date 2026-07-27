# ⭐ Experiment 1 — Basic Inheritance

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

class Dog(Animal):
    pass

dog = Dog("Mushu")

dog.eat()


# ⭐⭐ Experiment 2 — Using super()

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

car = Car("Tata", "Harrier")

print(f"Brand: {car.brand}")
print(f"Model: {car.model}")

# ⭐⭐⭐ Experiment 3 — Method Overriding


class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Some animal sound")

class Cat(Animal):
    def sound(self):
        print(f"{self.name} says Meow!")

cat = Cat("kitty")

cat.sound()


# ⭐⭐⭐⭐ Experiment 4 — isinstance() & issubclass()

print(isinstance(car, Car))
print(isinstance(car, Vehicle))
print(issubclass(Car, Vehicle))