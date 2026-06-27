# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ("apple", "banana", "orange", "coconut", "coconut")

print(len(fruits))
print("pineapple" in fruits)

print(fruits.index("banana"))
print(fruits.count("coconut"))

for fruit in fruits:
    print(fruit) 