# Union of Two Sorted Arrays
def union_array(arr1, arr2):
    i = 0
    j = 0
    merged = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            if not merged or merged[-1] != arr1[i]:
                merged.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            if not merged or merged[-1] != arr2[j]:
                merged.append(arr2[j])
            j += 1
        else:
            if not merged or merged[-1] != arr1[i]:
                merged.append(arr1[i])
            i += 1
            j += 1
        
    while i < len(arr1):
        if not merged or merged[-1] != arr1[i]:
            merged.append(arr1[i])
        i += 1

    while j < len(arr2):
        if not merged or merged[-1] != arr2[j]:
            merged.append(arr2[j])
        j += 1

    return merged

arr1 = [1,2,2,4]
arr2 = [2,3,4,5]

print(union_array(arr1, arr2))


# Intersection of Two Sorted Arrays

def intersection_array(arr1, arr2):
    i = 0
    j = 0
    merged = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            if not merged or merged[-1] != arr1[i]:
                merged.append(arr1[i])
            i += 1
            j += 1
        
    return merged
            

arr1 = [1,2,3,4,5]
arr2 = [2,4,6]

print(intersection_array(arr1, arr2))