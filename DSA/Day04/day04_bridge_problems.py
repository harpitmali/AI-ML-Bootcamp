# Problem 1 — Reverse Array In-Place

arr = [1,2,3,4,5,6]
start = 0

for i in range(len(arr)):
    if i > len(arr)-1-i:
        temp = arr[i]
        arr[i] = arr[len(arr)-1-i]
        arr[len(arr)-1-i] = temp
    

print(arr)

# Problem 2 — Check Equal Arrays

def arrays_equal(arr1, arr2):
    if len(arr1) != len(arr2):
        return False
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
            
    return True

arr1 = [1,2,3]
arr2 = [2,3]
print(arrays_equal(arr1, arr2))

# Problem 3 — Find Missing Number

arr = [1,2,3,4,5,6,8]
missing_value = -1
for i in range(len(arr)):
    if (i+1) != arr[i]:
        missing_value = (i+1)
    
print(f"Missing Value: {missing_value}")

# Problem 4 — First Repeating Element

def first_repeating_element(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                return arr[i]
    
    return -1

arr = [2,5,1,3,5,2]
print(first_repeating_element(arr))



# Bonus Challenge

def remove_duplicates(arr):
    i = 0

    while i < len(arr):
        j = i + 1

        while j < len(arr):
            if arr[i] == arr[j]:
                arr.pop(j)
            else:
                j += 1

        i += 1

    return arr


arr = [1, 2, 2, 3, 1, 4, 4]
print(remove_duplicates(arr))
