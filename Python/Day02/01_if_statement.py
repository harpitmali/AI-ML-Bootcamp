# if -> perform some code if some codition is right 
#       Else perform other code

age = int(input("Enter your Age: "))

if age >= 100:
    print("You are too old to sign up")
elif age > 18:
    print("You are now signed up!")
elif age < 0:
    print("You are not born yet!")
else:
    print("You must be 18+ to sign up")

# response program

response = input("Would you like some food? (Y/N) ")

if response == "Y":
    print("Have some food!")
else:
    print("No food for you!")


# Enter your name 

name = input("Enter your name: ")

if name == "":
    print("You did not type your name!")
else: 
    print(f"Hello {name}")



# Using boolean variable

online = False

if online:
    print("User is online!")
else: 
    print("User is offline!")