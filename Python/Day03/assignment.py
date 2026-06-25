# Assignment 1 — Name Analyzer

name = "harpit mali"

length = len(name)
first = name[0]
last = name[-1]
uppercase = name.upper()
lowercase = name.lower()
title_case = name.title()
reverse_string = name[::-1]

print(f"Length: {length}")
print(f"First Character: {first}")
print(f"Last Character: {last}")
print(f"Uppercase: {uppercase}")
print(f"Lowercase: {lowercase}")
print(f"Title Case: {title_case}")
print(f"Reverse: {reverse_string}")

# Assignment 2 — Palindrome Checker

palindrome_string = "madam"

reverse_string = palindrome_string[::-1]
if palindrome_string == reverse_string:
    print("Palindrome")
else:
    print("Not Palindrome")

# Assignment 3 — Username Validator

user_name = "harpit21"

first_character = user_name[0]

if len(user_name) < 5:
    print("Invalid Username")
elif not user_name.find(" ") == -1:
    print("Invalid Username")
elif not first_character.isalpha():
    print("Invalid Username")
else:
    print("Valid Username")

# Assignment 4 — Text Formatter
    
text = "hello world"

print(text.upper())
print(text.title())
print(text.lower())
print(text[::-1])

# Bonus Challenge

text = "Artificial Intelligence"
vowel_count = 0

for ch in text:
    if ch in "aeiouAEIOU":
        vowel_count += 1

print(f"No of Vowels : {vowel_count}")