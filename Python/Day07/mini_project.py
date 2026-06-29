def add_marks(marks):
    mark = int(input("Enter your Marks: "))
    if mark < 0:
        print("Marks can't be negative")
        return

    marks.append(mark)
    print("Marks added successfully.")

def display_marks(marks):
    if len(marks) == 0:
        print("No marks available.")
        return
    i = 1
    for mark in marks:
        print(f"{i}. {mark}")
        i += 1

def show_statistics(marks):
    if len(marks) == 0:
        print("No marks available.")
        return
    
    highest = find_maximum(marks)
    lowest = find_minimum(marks)
    average = find_average(marks)

    return highest, lowest, average

def show_passed_students(marks):
    passed_students = [mark for mark in marks if mark >= 40]
    if len(passed_students) == 0:
        print("No students passed.")
    else:
        print("Passed Student: ")
        display_marks(passed_students)

def show_distinction_students(marks):
    distinction_students = [mark for mark in marks if mark >= 75]
    if len(distinction_students) == 0:
        print("No Distinction Student")
    else:
        print("Distinction Student: ")
        display_marks(distinction_students)

def find_maximum(marks):
    highest = marks[0]
    for mark in marks:
        if mark > highest:
            highest = mark

    return highest

def find_minimum(marks):
    lowest = marks[0]
    for mark in marks:
        if mark < lowest:
            lowest = mark

    return lowest

def find_average(marks):
    total = 0
    for mark in marks:
        total += mark
    
    return total / len(marks)


marks = []

while True:
    print()
    print("===== Student Grade Analyzer =====")
    print("1. Add Marks")
    print("2. Display Marks")
    print("3. Show Statistics")
    print("4. Show Passed Students")
    print("5. Show Distinction Students")
    print("6. Exit")

    option = int(input("Enter the numer: "))

    if option == 1:
        add_marks(marks)

    elif option == 2:
        display_marks(marks)

    elif option == 3:
        stats = show_statistics(marks)

    if stats:
        highest, lowest, average = stats
        print(f"Highest: {highest}")
        print(f"Lowest: {lowest}")
        print(f"Average: {average}")
    
    elif option == 4:
        show_passed_students(marks)

    elif option == 5:
        show_distinction_students(marks)
    
    elif option == 6:
        print("Thank you!")
        break
    
    else:
        print("Invalid Input")
        print("Try Again!")