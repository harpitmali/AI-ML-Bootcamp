# conditional expression = one line shortcut for if-else statement (ternary operator)
#                          print or assign one or two values based on a condition
#                          X if condition else Y



num = -5
print("POSITIVE" if num > 0 else "NEGATIVE")


x = 10
print("EVEN" if x % 2 == 0 else "ODD")


a = 6
b = 7
max_num = a if a > b else b
min_num = a if a < b else b
print(f"Maximun number: {max_num}")
print(f"Minimum number: {min_num}")


age = 21
status = "Adult" if age >= 18 else "Child"
print(status)

temp = 25
weather = "Hot" if temp > 20 else "Cold"
print(weather)

user_role = "admin"
access_level = "Full Access" if user_role == "admin" else "Limited Access"
print(access_level)