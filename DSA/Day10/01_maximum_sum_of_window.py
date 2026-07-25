def maximum_sum_of_window(arr, k):
    if k <= 0 or k > len(arr):
        return None
    
    n = len(arr)
    current_sum = 0

    for i in range(k):
        current_sum += arr[i]
        
    max_sum = current_sum

    for i in range(k, n):
        current_sum += arr[i]
        current_sum -= arr[i-k]
        if current_sum > max_sum:
            max_sum = current_sum
    
    return max_sum

arr = [2,1,5,1,3,2]
k = 3

print(maximum_sum_of_window(arr, k))