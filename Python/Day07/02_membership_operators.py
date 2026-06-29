# Membership operators = used to test whether a value or variable found in sequence
#                        (string, list, tuple, set, or dictionary)
#                        1. in
#                        2. not in


seceret_word = "APPLE"

letter = input("Guess a letter in seceret word: ")

if letter.upper() in seceret_word:
    print(f"There is a {letter}")
else:
    print(f"{letter} was not found")



students = {"Luffy", "Zoro", "Sanji", "Ussop"}

student = input("Enter a name of student: ")

if student not in students:
    print(f"{student} was not Found")
else:
    print(f"{student} is a student")



grades = {
    "Luffy" : "D",
    "Zoro" : "C",
    "Sanji" : "A",
    "Ussop" : "B"
}

student = input("Enter student Name: ")

if student in grades:
    print(f"{student}'s grade: {grades[student]}")