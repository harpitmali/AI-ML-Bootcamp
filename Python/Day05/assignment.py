# Assignment 1 — Student Marks Manager

marks = [78, 92, 65, 88, 95]

total = marks[0]
highest = marks[0]
lowest = marks[0]

for i in range(1, len(marks)):
    if highest < marks[i]:
        highest = marks[i]

    if lowest > marks[i]:
        lowest = marks[i]
    
    total += marks[i]

print(f"Highest Value: {highest}")
print(f"Lowest Value: {lowest}")
print(f"Average Marks: {total/len(marks)}")

# Assignment 2 — Unique Visitors

visitors = [
    "Amit",
    "Rahul",
    "Amit",
    "Priya",
    "Rahul",
    "Kiran"
]

unique = set()

for name in visitors:
    unique.add(name)

print(f"Total Visitors : {len(visitors)}")
print(f"Unique Visitors : {len(unique)}")



# Assignment 3 — Tuple Challenge

student = ("Harpit", 20, "AI/ML")

print(f"Name: {student[0]}")
print(f"Age: {student[1]}")
print(f"Field: {student[2]}")

print("AI/ML" in student)



# Assignment 4 — Matrix Sum

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

total = 0

for row in matrix:
    for column in row:
        total += column

print(f"Matrix Sum: {total}")



# Bonus Challenge

matrix = [
    [1,2,3],
    [4,5,6]
]

for row in range(len(matrix[0])):
    for column in range(len(matrix)):
        print(matrix[column][row], end=" ")
    print()