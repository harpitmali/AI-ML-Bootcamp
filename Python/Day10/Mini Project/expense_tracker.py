import datetime

def add_expense():
    expense_name = input("Expense Name: ")
    category = input("Expense Category: ")
    amount = int(input("Amount: "))

    today = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    with open("expenses.txt", "a") as file:
        file.write(f"{today}, {category}, {expense_name}, {amount}\n")

def view_expense():
    try:
        with open("expenses.txt", "r") as file:
            lines = file.readlines()

        if not lines:
            print("No Expenses found")
        else:
            print("===== Expenses History =====")
            for i,line in enumerate(lines, start=1):
                date, category, expense, price  = line.strip().split(",")
                print(f"{i}.")
                print(f"Date: {date}")
                print(f"Category: {category}")
                print(f"Expense: {expense}")
                print(f"price: {price}\n")

    except FileNotFoundError:
        print("File Not Found")

def total_spending():
    try:
        with open("expenses.txt", "r") as file:
            lines = file.readlines()

        total = 0

        if not lines:
            print("No Expenses found")
        else:
            print("===== Expenses History =====")
            for i,line in enumerate(lines, start=1):
                date, category, expense, price  = line.strip().split(",")
                try:
                    price = int(price.strip())
                except ValueError:
                    print("There is problem in stroed Data")
                total += price
        
        print(f"Total Spent: {total}")

    except FileNotFoundError:
        print("File Not Found")

def highest_spending():
    try:
        with open("expenses.txt", "r") as file:
            highest_price = 0
            found = False

            for line in file:
                found = True

                date, category, expense, price = line.strip().split(",")
                try:
                    price = int(price.strip())
                except ValueError:
                    print("There is problem in stroed Data")

                if price > highest_price:
                    highest_price = price
                    highest_expense = expense.strip()
                    highest_date = date.strip()
                    highest_category = category.strip()
        
            if not found:
                    print("No expenses found.")
            else:
                print("=== Highest Expense ===")
                print(f"Date: {highest_date}")
                print(f"Category: {highest_category}")
                print(f"Expense: {highest_expense}")
                print(f"Amount: ₹{highest_price}")

    except FileNotFoundError:
        print("File Not Found")


while True:
    print("\n========= Expense Tracker =========")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Highest Expense")
    print("5. Exit\n")

    try:
        option = int(input("Enter Your Option: "))
    except ValueError:
        print("Wrong Value")
        continue

    match option:
        case 1:
            add_expense()
        case 2:
            view_expense()
        case 3:
            total_spending()
        case 4:
            highest_spending()
        case 5:
            print("Thank You")
            break
        case _:
            print("Wrong Input Try again!")

