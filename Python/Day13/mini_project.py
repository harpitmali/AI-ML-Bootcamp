class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, course, marks):
        super().__init__(name, age)
        self.course = course
        if 0 <= marks <= 100:
            self.marks = marks
        else:
            raise ValueError("Marks must be between 0 and 100.")
    
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
    
    def display_student(self):
        super().display_person()
        print(f"Course: {self.course}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.calculate_grade()}")

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display_employee(self):
        super().display_person()
        print(f"Salary: ₹{self.salary}")

class Professor(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.department = department

    def display_professor(self):
        super().display_employee()
        print(f"Department: {self.department}")


class Athlete:
    def __init__(self, sport):
        self.sport = sport

    def play(self):
        print(f"Playing {self.sport}")

class StudentAthlete(Student, Athlete):
    def __init__(self, name, age, course, marks, sport, medals):
        super().__init__(name, age, course, marks)
        Athlete.__init__(self, sport)
        self.medals = medals

    def display_all(self):
        super().display_student()
        print(f"Sport: {self.sport}")
        print(f"Medals: {self.medals}")


student1 = Student("Harpit", 21, "AI/ML", 98)
student2 = Student("Luffy", 23, "Data Science", 72)


professor1 = Professor("Garp", 30, 50000, "Civil Engineering")

studentAthlete1 = StudentAthlete("Zoro", 25, "Python", 65, "Football", 4)

print("===== UNIVERSITY REPORT =====")
print("-" * 40)
student1.display_student()
print("-" * 40)
student2.display_student()
print("-" * 40)
professor1.display_professor()
print("-" * 40) 
studentAthlete1.display_all()