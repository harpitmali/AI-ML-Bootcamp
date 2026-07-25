from datetime import datetime

# Assignment 1

name = input("Enter your Name: ")

print(f"Hello {name}")
print("Welcome to python")

# Assignment 2

born_year = int(input("Enter your born year "))

current_year = datetime.now().year
age = current_year - born_year

print(f"You are {age} years old")

# Assigment 3

celsius = float(input("Enter Celsius : "))

fahrenheit = ((9 / 5) * celsius) + 32

print(f"Celsius {round(celsius, 2)} equals to Fahrenheit {round(fahrenheit, 2)}")
