# Set = {} unordered and immutable, but add/remove OK. No Duplicates

fruits = {"apple", "banana", "orange", "coconut"}

print(len(fruits))
print("pineapple" in fruits)

fruits.add("pineapple")
fruits.remove("orange")
fruits.pop()
# fruits.clear()

print(fruits)