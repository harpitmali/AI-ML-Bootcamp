# input() - always returns strings

name = input("What is your name? :")
age = int(input("How old are you? :"))

# age = age + 1

print(f"Hello {name}")
print(f"You are {age} years old")


# Exercise 1 Calculating Area of Rectangle

length = float(input("Length = "))
width = float(input("Width = "))

area = length * width

print(f"Area = {area}cm")


# Exercise 2 Shopping Cart Program

item = input("What item would like to buy? :")
price = float(input("What is the price? :"))
quantity = int(input("how many would you like to buy? :"))

total = price * quantity
print(f"You have bought {quantity} X {item}/s")
print(f"Your Total is : {total}")