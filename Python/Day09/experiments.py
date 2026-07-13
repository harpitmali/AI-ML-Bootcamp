# Experiment 1 — Basic Exception Handling

try:
    num = int(input("Enter a number: "))
    print(100 / num)
except ValueError:
    print("Please enter a valid integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")


# Experiment 2 — Finally Block
    
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except Exception:
    print("Something went wrong.")
finally:
    print("Program Finished")

# Experiment 3 — File Detection
    
import os

path = "sample.txt"

if os.path.exists(path):
    print("File Found")
else:
    print("File Not Found")

# Experiment 4 — Writing Files

# with open("sample.txt", "w") as file:
#   file.write("Machine Learning")
    
# Experiment 5 — Reading Files
    
with open("sample.txt", "r") as file:
    print(file.read())

with open("sample.txt", "r") as file:
    print(file.readline())

with open("sample.txt", "r") as file:
    print(file.readlines())

# Bonus
    
with open("sample.txt", "a") as file:
    file.write("\nDeep Learning")