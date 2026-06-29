# List Comprehensions = A concise way to create lists in python
#                       Compact and easier to read than traditional loop
#                       [expression for value in iterable if condition]

double = [x * 2 for x in range(1, 11)]
thiple = [y * 3 for y in range(1, 11)]
square = [z * z for z in range(1, 11)]

print(double)
print(thiple)
print(square)




names = ["luffy", "zoro", "sanji", "chopper"]
names = [name.upper() for name in names]
first_character = [name[0] for name in names]

print(names)
print(first_character)




numbers = [1, -2, -4, 5, -6, 8, 10]
positive_numbers = [number for number in numbers if number >= 0]
negative_numbers = [number for number in numbers if number < 0]

print(positive_numbers)
print(negative_numbers)