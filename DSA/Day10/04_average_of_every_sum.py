def average_of_every_sum(arr, k):
    if k <= 0 or k > len(arr):
        return None
    
    n = len(arr)
    current_sum = 0
    new_arr = []

    for i in range(k):
        current_sum += arr[i]
        
    average = current_sum / k
    new_arr.append(round(average, 2))
    
    for i in range(k, n):
        current_sum += arr[i]
        current_sum -= arr[i-k]
        average = current_sum / k
        new_arr.append(round(average, 2))
    
    return new_arr

arr = [2,1,5,1,3,2]
k = 3

print(average_of_every_sum(arr, k))