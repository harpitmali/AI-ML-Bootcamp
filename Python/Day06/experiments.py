# Experiment 1 — Basic Function

def greet():
    print("Welcome to AI/ML Bootcamp!")

greet()
greet()

# Experiment 2 — Parameters

def greet(name):
    print(f"Hello {name}")

greet("Harpit")
greet("Champ")

# Experiment 3 — Return Value

def multiply(a, b):
    return a * b

result = multiply(6, 7)

print(result)

# Experiment 4 — Default Arguments

def power(base, exponent=2):
    return base ** exponent

print(power(5))
print(power(5, 3))

# Experiment 5 — Keyword Arguments

def introduce(name, age, city):
    print(f"{name}, {age}, {city}")

introduce(city="Jaipur", name="Harpit", age=20)

# Experiment 6 — *args

def total(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum

print(total(10, 20, 30, 40))

# Experiment 7 — **kwargs

def display(**student):
    for key, value in student.items():
        print(key, ":", value)

display(name="Harpit", age=20, field="AI/ML")