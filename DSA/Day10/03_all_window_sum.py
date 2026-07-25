def all_window_sum(arr, k):
    if k <= 0 or k > len(arr):
        return None
    
    n = len(arr)
    current_sum = 0
    windows_sum = []

    for i in range(k):
        current_sum += arr[i]
        
    windows_sum.append(current_sum)
    
    for i in range(k, n):
        current_sum += arr[i]
        current_sum -= arr[i-k]
        windows_sum.append(current_sum)
    
    return windows_sum

arr = [2,1,5,1,3,2]
k = 3

print(all_window_sum(arr, k))