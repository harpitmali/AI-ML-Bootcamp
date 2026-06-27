# Left Rotate by K

def left_rotate_k(arr, k):
    if len(arr) == 0:
        return arr
    
    k = k % len(arr)
    n = len(arr)
    start, end = 0, len(arr)-1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    start, end = 0, n-k-1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    
    start, end = n-k, len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return arr 


arr = [1,2,3,4,5]
k = 2

print(left_rotate_k(arr, k))




# right Rotate by K

def right_rotate_k(arr, k):
    k = k % len(arr)
    start, end = 0, len(arr)-1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    start, end = 0, k-1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    
    start, end = k, len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return arr 


arr = [1,2,3,4,5]
k = 2

print(right_rotate_k(arr, k))

# Find Leaders

def find_leaders(arr):
    leaders = []
    maximum_right = -1
    for i in range(len(arr)-1, -1, -1):
        if arr[i] >= maximum_right:
            leaders.append(arr[i])
            maximum_right = arr[i]
        
    leaders.reverse()
    return leaders
        


arr = [16,17,4,3,5,2]
print(find_leaders(arr))


# Maximum Difference

def maximum_difference(arr):
    max_diff = -1
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if j > i:
                if (arr[j] - arr[i]) >= max_diff:
                    max_diff = arr[j] - arr[i]
    
    return max_diff


arr = [2,3,10,6,4,8,1]
print(maximum_difference(arr))

# Bonus Challenge

def copy_array(arr):
    new_arr = []
    for i in range(len(arr)):
        new_arr.append(arr[i])
    
    return new_arr

arr = [10, 20, 30]
print(copy_array(arr))
