# Experiment 1 — Lists

fruits = ["apple", "banana", "mango"]

fruits.append("orange")
fruits.insert(1, "grapes")
fruits.remove("banana")

print(fruits)

# Experiment 2 — Sets

numbers = {1,2,3}

numbers.add(4)
numbers.add(2)

print(numbers)


# Experiment 3 — Tuples

colors = ("red", "green", "blue")

print(colors[1])
print(len(colors))
print("red" in colors)

# Experiment 4 — 2D Collections

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for row in matrix:
    print(row)

# Experiment 5 — Nested 2D Loop
    
matrix = [
    [1,2],
    [3,4]
]

for row in matrix:
    for value in row:
        print(value, end=" ")
    print()