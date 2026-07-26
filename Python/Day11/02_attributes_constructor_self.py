# Class
class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

# Creating Objects
dog1 = Dog("Mushu", 3, "Pemoriane")
dog2 = Dog("Hawk", 2, "Husky")

print(f"Name: {dog1.name}, Age: {dog1.age}, Breed: {dog1.breed}")
print(f"Name: {dog2.name}, Age: {dog2.age}, Breed: {dog2.breed}")
