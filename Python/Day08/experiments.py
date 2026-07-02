# Experiment 1 — Match-Case

day = 2

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid")


# Experiment 2 — Local vs Global Scope
        
x = 100

def demo():
    x = 50
    print("Inside:", x)

demo()

print("Outside:", x)


# Experiment 3 — Create Your Own Module

import mymath

print(mymath.square(5))
print(mymath.cube(3))

# Experiment 4 — Import Specific Function

from mymath import square

print(square(8))

