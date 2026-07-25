# Problem 1 — Second Smallest

def second_smallest(arr):
    min = arr[0]
    second_min = arr[1]

    if second_min < min:
        second_min, min = min, second_min

    for num in arr[2:]:
        if num < min:
            second_min, min = min, num
        elif num != min and (second_min == min or num < second_min):
            second_min = num

    return second_min


arr = [5, 2, 8, 1, 4]
print(second_smallest(arr))

# Problem 2 — Check Rotation

def check_rotation(arr1, arr2):
    if len(arr1) != len(arr2):
        return False

    added_array = arr1 + arr1
    n = len(arr1)

    for i in range(n):
        match = True

        for j in range(n):
            if added_array[i+j] != arr2[j]:
                match = False
                break

        if match:
            return True
        
    return False

arr1 = [1,2,3,4,5]
arr2 = [3,4,5,1,2]

print(check_rotation(arr1, arr2))

# Problem 3 — Move Negative Numbers to End

def move_negative_number(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j] < 0:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

arr = [3, -2, 5, -1, 7]
print(move_negative_number(arr))

# Bonus Problem 

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def rotate_left(arr, k):
    n = len(arr)
    k %= n

    reverse(arr, 0, k - 1)
    reverse(arr, k, n - 1)
    reverse(arr, 0, n - 1)

    return arr


arr = [1, 2, 3, 4, 5]
print(rotate_left(arr, 2))