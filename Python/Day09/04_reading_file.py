# Python reading file (.txt, .csv, .json)

# Reading text file
file_path = "output.txt"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found")

# Reading Json File

import json

file_path = "output.json"
try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content)
        print(content["name"])
except FileNotFoundError:
    print("File not found")

# Reading csv file

import csv

file_path = "output.csv"
try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)
except FileNotFoundError:
    print("File not found")