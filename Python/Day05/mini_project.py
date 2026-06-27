students = []

while True:
    print("===== Student Record Manager =====")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Search Student")
    print("4. Display Students")
    print("5. Exit")
    
    option = int(input("Choose: "))

    if option == 1:
        name = input("Enter student name: ")
        students.append(name)
        print("Student Added Successfully!")
    
    elif option == 2:
        name = input("Enter student name: ")
        if name in students:
            students.remove(name)
            print("Student Removed.")
        else:
            print("Student Not Found.")
    
    elif option == 3:
        name = input("Enter student name: ")
        if name in students:
            print("Student Exists.")
        else:
            print("Student Not Found.")

    elif option == 4:
        i = 1
        if len(students) > 0:
            for name in students:
                print(i, name)
                i += 1
        else:
            print("No students available.")

    elif option == 5:
        print("Thank you!")
        break

    else:
        print("Invalid choice.")