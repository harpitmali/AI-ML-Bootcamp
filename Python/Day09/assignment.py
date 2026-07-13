# Assignment 1 — Safe Calculator

try:
    num1 = int(input("Enter first number: "))
    operator = input("Enter Operator (+,-,*,/): ")
    num2 = int(input("Enter Second number: "))

    match operator:
        case '+':
            print(num1 + num2)
        case '-':
            print(num1 - num2)
        case '*':
            print(num1 * num2)
        case '/':
            print(num1 / num2)
        case _:
            print("Wrong input for Operator.")

except ValueError:
    print("Invalid Number")
except ZeroDivisionError:
    print("Division by Zero not possible")
finally:
    print("Program Finished")

# Assignment 2 — Notes Writer

with open("notes.txt", "a") as file:
    notes = input("Enter your note: ")
    file.write(f"\n{notes}")



# Assignment 3 — Notes Reader

try:
    with open("notes.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("No notes found.")
finally:
    print("Program Finished")

    


# Assignment 4 — Student File Manager

def add_students(name):
    with open("students.txt", "a") as file:
        file.write(f"{name}\n")

def read_students():
    try:
        with open("students.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No students found.")

try:

    while True:
        print("\n===== Student File Manager =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit \n")

        option = int(input("Enter your Choise: "))
        match option:
            case 1:
                name = input("Enter student name: ")
                add_students(name)
            case 2:
                read_students()
            case 3:
                break
            case _:
                print("Wrong Input Try again")


except ValueError:
    print("Wrong Value")
finally:
    print("Program Finished")



# Bonus Challenge

def add_diary(entry):
    with open("diary.txt", "a") as file:
        file.write(f"\n--------------------\n{entry}")

def read_diary():
    try:
        with open("diary.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No Diary found.")


try:

    while True:
        print("\n===== Personal Diary =====")
        print("1. Write Entry")
        print("2. Read Diary")
        print("3. Exit \n")

        option = int(input("Enter your Choise: "))
        match option:
            case 1:
                entry = input("Today's Entery: ")
                add_diary(entry)
            case 2:
                read_diary()
            case 3:
                break
            case _:
                print("Wrong Input Try again")


except ValueError:
    print("Wrong Value")
finally:
    print("Program Finished")