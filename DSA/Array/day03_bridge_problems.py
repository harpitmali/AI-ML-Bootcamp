# Problem 1 — Rotate Left by One

def rotate_left(arr):
    first_element = arr[0]
    length = len(arr)

    for i in range(len(arr)-1):
        arr[i] = arr[i+1]
    
    arr[length-1] = first_element
    return arr


# Problem 2 — Rotate Right by One

def rotate_right(arr):
    last_element = arr[len(arr)-1]

    for i in range(len(arr)-1, 0, -1):
        arr[i] = arr[i-1]
    
    arr[0] = last_element
    return arr

# Problem 3 — Merge Two Arrays

def merge_arrays(arr1, arr2):
    combined_length = len(arr1) + len(arr2)
    for i in range(len(arr2)):
        arr1.append(arr2[i])
    
    return arr1

# Problem 4 — Remove All Occurrences

def remove_occurrences(arr, target):
    new_arr = []
    for i in range(len(arr)):
        if arr[i] != target:
            new_arr.append(arr[i])

    return new_arr

# Bonus Challenge

def insert_sorted(arr, value):
    new_arr = []
    inserted = False
    for i in range(len(arr)):
        if arr[i] > value:
        
            for j in range(i):
                new_arr.append(arr[j])
            
            new_arr.append(value)
            inserted = True
            
            for k in range(i, len(arr)):
                new_arr.append(arr[k])
            
            break

    if not inserted:
        for i in range(len(arr)):
            new_arr.append(arr[i])
        new_arr.append(value)

    return new_arr




arr = [1, 2, 3, 4]
print(rotate_left(arr))

arr = [1, 2, 3, 4]
print(rotate_right(arr))

arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
print(merge_arrays(arr1, arr2))

arr = [2, 1, 2, 3, 2, 5]
print(remove_occurrences(arr, 2))

arr = [10, 20, 30, 40]
print(insert_sorted(arr, 25))