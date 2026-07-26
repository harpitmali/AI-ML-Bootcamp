def prefix_sum_array(arr):
    prefix = [0] * len(arr)
    prefix[0] = arr[0]
    
    for i in range(1, len(arr)):
        prefix[i] = prefix[i-1] + arr[i]
    
    return prefix

def range_sum(prefix, start, end):
    if start == 0:
        total = prefix[end]
    else:
        total = prefix[end] - prefix[start-1]

    return total

arr = [4, 2, 7, 1, 5]
print(prefix_sum_array(arr))
prefix = prefix_sum_array(arr)

print(range_sum(prefix, 1, 3))