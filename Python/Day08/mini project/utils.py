def display_employee(employees):
    if len(employees) == 0:
        print("No data recorded yet")
    i = 1
    for employee in employees:
        print(f"Employee {i}")
        print("--------------")
        for key, value in employee.items():
            print(f"{key}: {value}")
        i += 1
    

def display_salary(gross_salary, bonus, tax, final_salary):
    print(f"Gross Salary : {gross_salary}")
    print(f"Bonus : {bonus}")
    print(f"Tax : {tax}")
    print(f"Final Salary : {final_salary}")