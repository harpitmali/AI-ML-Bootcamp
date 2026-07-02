import salary
import utils

employees = []

def add_employee(employees):
    name = input("Enter Employee Name: ")
    for employee in employees:
        if employee["name"] == name:
            print("Employee already exists.")
            return

    hours = int(input("Enter Hours Worked: "))
    rate = float(input("Enter rate: "))

    if hours < 0:
        print("Hours cannot be negative.")
        return

    if rate < 0:
        print("rate can't be negative.")
        return

    employee = {
        "name" : name, 
        "hours" : hours,
        "rate" : rate
    }

    employees.append(employee)

def checking_employee(name):
    found = False

    for employee in employees:
        if employee["name"] == name:
            found = True

            hours = employee["hours"]
            rate = employee["rate"]

            gross_salary, bonus, tax, final_salary = salary.net_salary(hours, rate)

            utils.display_salary(gross_salary, bonus, tax, final_salary)
            break

    if not found:
        print("Employee not found.")

while True:
    print()
    print("===== Employee Salary Calculator =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Calculate Salary")
    print("4. Exit")
    print()

    option = int(input("Enter the number: "))

    match option:
        case 1:
            add_employee(employees)
            print("Employee added successfully.")
        case 2:
            utils.display_employee(employees)
        case 3:
            if len(employees) == 0:
                print("No employee data recored yet.")
            else:
                name = input("Enter employee name: ")
                checking_employee(name)
        case 4:
            print("Thank You!")
            break
        case _:
            print("Invalid Input")
            print("Try again!")