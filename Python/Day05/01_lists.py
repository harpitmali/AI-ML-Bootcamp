# collection = single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicates OK

fruits = ["apple", "banana", "orange", "coconut"]

print(fruits)
print(fruits[0])
print(fruits[-2])
print(fruits[:3])
print(fruits[::2])
print(fruits[::-1])
print(len(fruits))
print("apple" in fruits)

# fruits[0] = "pineapple"
# fruits.remove("orange")
# fruits.insert(2, "mango")
# fruits.sort()
# fruits.reverse()
# fruits.clean()
# print(fruits.index("mango"))
# print(fruits.count("apple"))

for fruit in fruits:
    print(fruit)

# print(dis(fruits))
# print(help(fruits))