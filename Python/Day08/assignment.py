# Assignment 1 — Calculator using Match-Case

def calculator(a, b, operator):
    match operator:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            if b == 0:
                return "B can't be zero"
            else:
                return a / b
        case _:
            return "Invalid Operator"

a = int(input("Enter Value of A: "))
b = int(input("Enter Value of B: "))
operator = input("Enter Operation you want perform (+, -, *, /) : ")


print(calculator(a, b, operator))

# Assignment 2 — Create Your Own Math Module

import mymath

print(mymath.add(5, 3))
print(mymath.subtract(5, 3))
print(mymath.multiply(5, 3))
print(f"{mymath.divide(5, 3):.2f}")


# Assignment 3 — Scope Practice

x = 50

def demo():
    x = 25
    print(x)

demo()

print(x)

# Assignment 4 — __main__

import demo

print("Finished")

# ⭐ Bonus Challenge

import geometry

print(geometry.area_square(10))
print(geometry.area_rectangle(4, 7))
print(geometry.area_circle(4))
