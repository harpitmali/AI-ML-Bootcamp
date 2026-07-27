# ⭐ Experiment 1 — Basic Dictionary

def print_dict(my_dict):
    for key, value in my_dict.items():
        print(f"{key}: {value}")

student = {
    "name": "Harpit",
    "age": 21,
    "course": "AI/ML"
}

print("=== Before ===")
print_dict(student)

student["age"] = 22
student["city"] = "Ahemdabad"
print()

print("=== After ===")
print_dict(student)

# ⭐⭐ Experiment 2 — Check Existence

marks = {
    "Math": 95,
    "Python": 98
}

print(True if "Python" in marks else False)
print(True if "Science" in marks else False)


# ⭐⭐⭐ Experiment 3 — Frequency Counter

def frequency_count(arr):
    frequency = {}

    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    return frequency

arr = [5, 3, 5, 2, 3, 5, 1]

print(frequency_count(arr))

# ⭐⭐⭐⭐ Experiment 4 — Most Frequent Element

frequency = frequency_count(arr)
most_frequent_count = 0
most_frequent = None

for key, value in frequency.items():
    if value > most_frequent_count:
        most_frequent = key
        most_frequent_count = value

    
print(f"{most_frequent}: {frequency[most_frequent]}")