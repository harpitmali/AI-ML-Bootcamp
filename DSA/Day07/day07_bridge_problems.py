# Problem 1 — Lower Bound

def lower_bound(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] >= target:
            high = mid - 1
        else:
            low = mid + 1
        
    return low


arr = [2,5,5,8,10]
target = 5

print(lower_bound(arr, target))

# Problem 2 - Upper Bound

def upper_bound(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] <= target:
            low = mid + 1
        else:
            high = mid - 1
        
    return low

arr = [2,5,5,8,10]
target = 5

print(upper_bound(arr, target))

# Problem 3 — Floor of a Number

def floor_of_numbers(arr, target):
    low = 0
    high = len(arr) - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] <= target:
            low = mid + 1
            ans = arr[mid]
        else:
            high = mid - 1
        
    return ans

arr = [2,5,8,12,16]
target = 5

print(floor_of_numbers(arr, target))


# Problem 4 — Ceiling of a Number

def ceiling_of_number(arr, target):
    low = 0
    high = len(arr) - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] >= target:
            high = mid - 1
            ans = arr[mid]
        else:
            low = mid + 1
        
    return ans


arr = [2,5,8,12,16]
target = 7

print(ceiling_of_number(arr, target))

# Bonus Challenge

def binary_search_first_occurance(arr, target):
    low = 0
    high = len(arr) - 1
    first = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            high = mid - 1
            first = mid
        elif target > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    
    return first

def binary_search_last_occurance(arr, target):
    low = 0
    high = len(arr) - 1
    last = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            low = mid + 1
            last = mid
        elif target > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    
    return last

def bonus_challenge(arr, target):
    first = binary_search_first_occurance(arr, target)
    if first == -1:
        return (-1, -1)

    last = binary_search_last_occurance(arr, target)

    return (first, last)

arr = [1,2,4,4,4,6,8]
target = 4

print(bonus_challenge(arr, target))