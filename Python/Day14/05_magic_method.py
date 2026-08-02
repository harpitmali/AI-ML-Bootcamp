# 1. __init__()

class Student:
    def __init__(self, name):
        self.name = name

student = Student("Harpit")

print(student.name)

# 2. __str__()

class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student({self.name})"
    
student = Student("Harpit")

print(student)


# 3. __len__()

class Team:
    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)
    
team = Team(["a", "b", "c"])

print(len(team))

# 4. __add__()

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value
    
a = Number(10)
b = Number(20)

c = a + b
print(c)

# 5. __eq__()

class Student:
    def __init__(self, marks):
        self.marks = marks

    def __eq__(self, other):
        return self.marks == other.marks
    
student1 = Student(95)
student2 = Student(95)

print(student1 == student2)