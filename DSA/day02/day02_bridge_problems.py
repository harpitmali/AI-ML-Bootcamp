# Problem 1 — Count Occurrences

def count_occurrences(arr, target):
    total = 0
    for num in arr:
        if num == target:
            total += 1
        
    return total

# Problem 2 — Check if Array is Sorted

def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
        
    return True

# Problem 3 — Find Smallest Element Index

def smallest_index(arr):
    num = arr[0]
    index = 0
    for i in range(len(arr)):
        if num > arr[i]:
            num = arr[i]
            index = i
        
    return index

# Problem 4 — Check Duplicate

def has_duplicate(arr):
    ans = False
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                ans = True
    
    return ans

# Bonus Challenge

def move_zeroes_to_end(arr):

    for i in range(len(arr)):
        if arr[i] == 0:
            for j in range(i+1, len(arr)):
                if arr[j] != 0:
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp
                    break
    
    return arr

arr = [5, 0, 2, 0, 8]

print(count_occurrences(arr, 0))
print(is_sorted(arr))
print(smallest_index(arr))
print(has_duplicate(arr))
print(move_zeroes_to_end(arr))