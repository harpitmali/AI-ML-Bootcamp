"""# Assignment 1 — Multiplication Table

num = int(input("Enter a number : "))

for i in range(1, 11):
    print(f"{num} X {i} = {num * i} ")

# Assignment 2 — Number Guessing Game
    
num = 21
guess = int(input("Guess a number between 1-100 : "))

while num != guess:
    print("You guessed it wrong")
    print("Try again!")
    guess = int(input("Guess a number between 1-100 : "))

print("You guessed it right")

# Assignment 3 — Sum of First N Numbers

num = int(input("Enter a number : "))
total = 0

for i in range(1, num+1):
    total += i

print(f"Sum of first {num} is {sum}")

# Assignment 4 — Star Pyramid

num = int(input("Enter a number : "))

for i in range(1, num+1):
    for k in range(num-i, 0, -1):
        print(end=" ")

    for j in range(i):
        print("*", end="")

    for l in range(0, i-1):
        print("*", end="")
    print()"""


# Anagram function

def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    for ch in str1:
        if str1.count(ch) != str2.count(ch):
            return False
    
    return True

str1 = input("Enter a string: ")
str2 = input("Enter another string: ")

check = is_anagram(str1, str2)
if check:
    print("They are anagrams.")
else:
    print("They are not anagrams.")
