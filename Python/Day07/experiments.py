# Experiment 1 — Iterate Through Different Collections
numbers = [10, 20, 30]
name = "Harpit"
colors = ("red", "green", "blue")

for num in numbers:
    print(num)

for ch in name:
    print(ch)

for color in colors:
    print(color)

# Experiment 2 — Membership Operator
fruits = ["apple", "banana", "mango"]

print("banana" in fruits)
print("orange" in fruits)
print("apple" not in fruits)

# Experiment 3 — Basic List Comprehension
numbers = [1,2,3,4,5]

squares = [x*x for x in numbers]

print(squares)

# Experiment 4 — Filtering
numbers = [1,2,3,4,5,6,7,8]

even = [x for x in numbers if x % 2 == 0]

print(even)

# Experiment 5 — String Transformation
names = ["harpit", "champ", "python"]

upper_names = [name.upper() for name in names]

print(upper_names)