# Problem 1 — Count Iterations

def binary_search_steps(arr, target):
    low = 0
    high = len(arr) - 1
    steps = 0

    while low <= high:
        mid = (low+high) // 2

        if arr[mid] == target:
            steps += 1
            return steps
        elif target > arr[mid]:
            steps += 1
            low = mid + 1
        else:
            steps += 1
            high = mid - 1

    return -1

arr = [2,5,8,12,16,23,38,56,72]

print(binary_search_steps(arr, 38))

# Problem 2 — Binary Search Boolean

def binary_search_exists(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low+high) // 2

        if arr[mid] == target:
            return True
        elif target > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1


    return False

print(binary_search_exists(arr, 72))

# Problem 3 — Find Insertion Position

def find_inserted_position(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low+high) // 2

        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1


    return low

arr = [2,5,8,12,16,23]

target = 10

print(find_inserted_position(arr, target))

# Problem 4 — Binary Search on Descending Array

def binary_search_desending_array(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low+high) // 2

        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            high = mid - 1
        else:
            low = mid + 1


    return -1


arr = [90,80,70,60,50,40,30]

print(binary_search_desending_array(arr, 40))

# Bonus Challenge — First Occurrence

def binary_search_first_occurance(arr, target):
    low = 0
    high = len(arr) - 1
    first_occurance = -1

    while low <= high:
        mid = (low+high) // 2

        if arr[mid] == target:
            first_occurance = mid
            high = mid - 1
        elif target > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1


    return first_occurance

arr = [2,5,5,5,8,8,12]
print(binary_search_first_occurance(arr, 8))