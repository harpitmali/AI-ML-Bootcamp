# Last Occurance

def binary_search_last_occurance(arr, target):
    low = 0
    high = len(arr) - 1
    last_occurance = -1

    while low <= high:
        mid = (low+high) // 2

        if arr[mid] == target:
            last_occurance = mid
            low = mid + 1
        elif target > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1
    
    return last_occurance

arr = [2,5,5,5,8,8,12]
last_occurance = binary_search_last_occurance(arr, 5)
print(last_occurance)


# First Occurance

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
first_occurance = binary_search_first_occurance(arr, 5)
print(first_occurance)

# Count Occurance

def count_occurrences(arr, target):
    
    first = binary_search_first_occurance(arr, target)
    if first == -1:
        return 0

    last = binary_search_last_occurance(arr, target)
    
    return (last-first+1)

arr = [2,5,5,5,8,8,12]
print(count_occurrences(arr, 8))