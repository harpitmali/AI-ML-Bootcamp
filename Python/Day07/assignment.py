# Assignment 1 — Count Vowels

def count_vowels(text):
    count = 0
    for ch in text:
        if ch in "aeiouAEIOU":
            count += 1
    return count

text = "I love watching One Piece"
print(count_vowels(text))

# Assignment 2 — Even Numbers

numbers = [3,8,12,5,7,10,14]

even_numbers = [x for x in numbers if x % 2 == 0]

print(even_numbers)

# Assignment 3 — Name Formatter

names = ["harpit","champ","python","machine learning"]

title_name = [name.title() for name in names]

print(title_name)

# Assignment 4 — Positive Numbers

numbers = [-5,10,-2,8,0,-7,3]

positive_numbers = [num for num in numbers if num >= 0]

print(positive_numbers)

# ⭐ Bonus Challenge

words = ["apple","AI","banana","ML","python","C"]

selected_word = [word.upper() for word in words if len(word) >= 3]

print(selected_word)