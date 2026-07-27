class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, course, marks):
        super().__init__(name, age)
        self.course = course
        if 0 <= marks <= 100:
            self.marks = marks
        else:
            raise ValueError("Marks must be between 0-100")

    def calculate_grade(self):
        if self.marks >= 90:
            grade = "A"
        elif self.marks >= 80:
            grade = "B"
        elif self.marks >= 70:
            grade = "C"
        elif self.marks >= 60:
            grade = "D"
        else:
            grade = "F"
        
        return grade

    def is_pass(self):
        return "Pass" if self.marks >= 40 else "Fail"
        
    def display_info(self):
        super().display_info()
        print(f"Course: {self.course}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.calculate_grade()}")
        print(f"Status: {self.is_pass()}")

student1 = Student("Harpit", 21, "AI/ML", 97)

student2 = Student("Luffy", 20, "Data Science", 77)

student3 = Student("Zoro", 23, "Web Development", 67)

student1.display_info()
print()
student2.display_info()
print()
student3.display_info()
print()

print("Topper: ")
if student1.marks > student2.marks and student1.marks > student3.marks:
    print(f"{student1.name}")
    print(f"Marks: {student1.marks}")
elif student2.marks > student3.marks and student2.marks > student1.marks:
    print(f"{student2.name}")
    print(f"Marks: {student2.marks}") 
elif student3.marks > student1.marks and student3.marks > student2.marks:
    print(f"{student3.name}")
    print(f"Marks: {student3.marks}")
elif student1.marks == student2.marks and student1.marks > student3.marks:
    print(f"{student1.name} and {student2.name}")
    print(f"Marks: {student1.marks}")
elif student2.marks == student3.marks and student2.marks > student1.marks:
    print(f"{student2.name} and {student3.name}")
    print(f"Marks: {student2.marks}")
elif student1.marks == student3.marks and student1.marks > student2.marks:
    print(f"{student1.name} and {student3.name}")
    print(f"Marks: {student1.marks}")
else:
    print(f"{student1.name}, {student2.name} and {student3.name}")
    print(f"Marks: {student1.marks}")