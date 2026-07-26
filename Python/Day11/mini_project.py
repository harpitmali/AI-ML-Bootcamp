class Student:
    def __init__(self, name, roll_no, course, marks):
        self.name = name
        self.roll_no = roll_no
        self.course = course
        self.marks = marks

    def display_student(self):
        print("\n========== Student ==========\n")
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Course: {self.course}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.calculate_grade()}")
        if self.is_pass():
            print("Pass")
        else:
            print("Fail")
        print()

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

    def update_marks(self, new_marks):
        if 0 <= new_marks <= 100:
            self.marks = new_marks
            print("Marks Updated Successfully!")
        else:
            print("Invalid Marks")
    
    def is_pass(self):
        return self.marks >= 40
    

student1 = Student("Harpit", 51, "AI/ML", 95)
student2 = Student("Luffy", 11, "Data Science", 39)
student3 = Student("Zoroo", 75, "Web Development", 75)

student1.display_student()
student2.display_student()
student3.display_student()

student2.update_marks(55)
student2.display_student()

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