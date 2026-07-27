class Animal:
    pass

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog()
cat = Cat()

print("====isinstance()====")
print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
print(isinstance(dog, Cat))
print(isinstance(dog, object))

print()

print("====issubclass()====")
print(issubclass(Dog, Animal))
print(issubclass(Cat, Animal))
print(issubclass(Animal, Dog))
print(issubclass(Dog, object))