# Assignment 1 — Voting Eligibility Checker

name = input("Enter your Name: ")
age = int(input("Enter your Age: "))
citizenship = input("Are you citizen of this Country? (Y/N)").upper()

if age >= 18 and citizenship == "Y":
    print(f"Hello {name}!")
    print("You are eligible to vote.")
else:
    print(f"Sorry {name}, you are not eligible to vote")

# Assignment 2 — Login System
    
username = "admin"
password = "python123"

entered_username = input("Enter Username: ")
entered_password = input("Enter Password: ")

if entered_username == username and entered_password == password:
    print("Login Successful")
else:
    print("Invalid Username or Password")



# Assignment 3 — Number Classifier

num = int(input("Enter a Number: "))

if num == 0:
    print("Zero")
elif num > 0:
    print("Positive")
else:
    print("Negative")

if num % 2 == 0:
    print("Even")
else:
    print("Odd")



# Assigmnet 4 - Student Grade System

marks = int(input("Enter your Marks: "))

if 90 <= marks <= 100:
    print("Grade A")
elif 80 <= marks <= 89:
    print("Grade B")
elif 70 <= marks <= 79:
    print("Grade C")
elif 60 <= marks <= 69:
    print("Grade D")
elif 0 <= marks <= 59:
    print("Fail")
else:
    print("Invalid Marks")



# Assignment 5 — Largest of Three Numbers

a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))

if a > b and a > c:
    print(f"Largest value A: {a}")
elif b > a and b > c:
    print(f"Largest value B: {b}")
elif c > a and c > b:
    print(f"Largest value C: {c}")
elif a == b and a > c:
    print(f"Both A: {a} and B: {b} are largest")
elif a == c and a > b:
    print(f"Both A: {a} and C: {c} are Largest")
elif b == c and b > a:
    print(f"Both B: {b} and C: {c} are Largest")
elif a == b == c:
    print("All numbers are equal")



# Bonus Challenge

password = input("Enter a strong Password: ")

if len(password) >= 8:
    print("This is Strong Password")
else:
    print("This is not a Strong password")