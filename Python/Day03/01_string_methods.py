# name = input("Enter your full name: ")
phone_number = input("Enter Your phone number: ")

# result = len(name)
# result = name.find("a")
# result = name.rfind("a")
# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# result = name.isdigit()
# result = name.isalpha()
# result = phone_number.count("3")
phone_number = phone_number.replace("3", "5")

print(phone_number)


# validate user input execersice
# 1. no more than 12 characters
# 2. no space
# 3. no digits

user_name = input("Enter your username: ")

if len(user_name) > 12:
    print("Your username can't be more than 12 characters")
elif not user_name.find(" ") == -1:
    print("Your username can't contain space")
elif not user_name.isalpha():
    print("Your username can't contain digit")
else:
    print(f"Welcome {user_name}")