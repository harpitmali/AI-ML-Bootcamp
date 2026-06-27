fruits = ["apple", "banana", "orange", "coconut"]
vegetable = ["carrot", "patato", "tamato"]
meats = ["chicken", "turkey", "steak"]

groceries = [fruits, vegetable, meats]
# we can also do this 
# groceries = [["apple", "banana", "orange", "coconut"],
#              ["carrot", "patato", "tamato"]
#              ["chicken", "turkey", "steak"]]

print(groceries[0])
print(groceries[1])
print(groceries[0][2])
print(groceries[2][0])

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()        
