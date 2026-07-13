def add_contact(name, number):
    with open("contacts.txt", "a") as file:
        file.write(f"{name},{number}\n")

def view_contact():
    try:
        with open("contacts.txt", "r") as file:
            lines = file.readlines()

        if len(lines) == 0:
            print("No Contacts found.")
        else:
            print("===== Contacts =====")
            for i, line in enumerate(lines, start=1):
                name, number = line.strip().split(",")
                print(f"{i}.")
                print("Name:", name)
                print("Number:", number)
                print()

    except FileNotFoundError:
        print("File not found")

def search_contact():
    search_name = input("Enter name: ")
    found = False
    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                name, number = line.strip().split(",")

                if name.lower() == search_name.lower():
                    print("Name: ", name)
                    print("Number: ", number)
                    found = True
                    break
        
        if not found:
            print("Contact Not Found")
    except FileNotFoundError:
        print("File not Found")

def delete_contact():
    delete_name = input("Enter name: ")
    found = False
    new_data = []

    try:
        with open("contacts.txt", "r") as file:
            lines = file.readlines()

        if len(lines) == 0:
            print("No Contacts found.")
            return

        for line in lines:
            name, number = line.strip().split(",")

            if name.lower() == delete_name.lower():
                found = True
            else:
                new_data.append(line)

        with open("contacts.txt", "w") as file:
            file.writelines(new_data)

        if found:
            print("Record Deleted Successfully.")
        else:
            print("Contact not found.")
    except FileNotFoundError:
        print("File not Found")

try:
    while True:
        print("\n===== Contact Book =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit\n")

        option = int(input("Enter Your Option: "))

        match option:
            case 1:
                name = input("Enter Name: ")
                number = input("Enter Phone Number: ")
                add_contact(name, number)
                print("Contact added successfully.")
            case 2:
                view_contact()
            case 3:
                search_contact()
            case 4:
                delete_contact()
            case 5:
                print("Thank You!")
                break
            case _:
                print("Wrong Input Try again!")

except ValueError:
    print("Wrong Value")