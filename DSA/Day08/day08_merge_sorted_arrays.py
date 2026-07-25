def merge_sorted_array(arr1, arr2):
    i = 0
    j = 0
    merged = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            merged.append(arr2[j])
            j += 1
        else:
            merged.append(arr1[i])
            i += 1
            merged.append(arr2[j])
            j += 1
        
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged

arr1 = [1,3,5]
arr2 = [1,3,6]

print(merge_sorted_array(arr1, arr2))


# Remove Duplicates from sorted array

def  remove_duplicates(arr):
    i = 0
    
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i+= 1
            arr[i] = arr[j]

    return arr[:i+1]

arr = [1,1,2,2,3,4,4,5]
print(remove_duplicates(arr))


# Bonus Challenege

def merge_three_sorted_array(arr1, arr2, arr3):
    temp = merge_sorted_array(arr1, arr2)
    ans = merge_sorted_array(temp, arr3)
    return ans

arr1 = [1,4,5]
arr2 = [2,5]
arr3 = [3,6]

print(merge_three_sorted_array(arr1, arr2, arr3))