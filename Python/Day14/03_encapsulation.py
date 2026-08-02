# Public Members

class Student:
    def __init__(self, name):
        self.name = name

student = Student("Harpit")

print(student.name)

# Protected Members


class Student:
    def __init__(self, marks):
        self._marks = marks

student = Student(80)

print(student._marks)

student._marks = 95

print(student._marks)

# Private Members
 
class Student:
    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):
        print(self.__marks)

student = Student(98)

student.get_marks()

print(student._Student__marks)