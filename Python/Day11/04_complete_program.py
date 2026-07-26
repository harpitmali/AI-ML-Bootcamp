class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")

student1 = Student("Harpit", 21, "AI/ML")
student2 = Student("Krish", 20, "Data Science")

student1.introduce()
print()
student2.introduce()