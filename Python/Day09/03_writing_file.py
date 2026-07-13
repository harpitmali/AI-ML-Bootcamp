# Python file writing (.txt, .json, .csv)

# Working with json file

employees = ["luffy", "zoro", "Ussop", "Sanji", "Franky", "Brook"]

file_path = "output.txt"

with open(file_path, "w") as file:
    for employee in employees:
        file.write(employee + "\n")
    print(f"The file '{file_path}' Exists")


# Working with json file
import json

employees = {
    "name": "Harpit",
    "age": 21,
    "Job": "AI/ML"
}

file_path = "output.json"

with open(file_path, "w") as file:
    json.dump(employees, file, indent=4)
    print(f"The file '{file_path}' Exists")



# Working with csv file
    
import csv

employees = [["Name", "Age", "Job"],
             ["Harpit", 21, "AI/ML"],
             ["Luffy", 18, "Pirate"],
             ["Zoro", 22, "Swordsman"]]

file_path = "output.csv"

with open(file_path, "w") as file:
    writer = csv.writer(file)
    for row in employees:
        writer.writerow(row)
    print(f"The file '{file_path}' Exists")