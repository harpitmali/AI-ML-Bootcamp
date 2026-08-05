"""def maximum_average_subarray(nums, k):
    if k <= 0 or k > len(nums):
        return None
    
    n = len(nums)
    current_sum = 0

    for i in range(k):
        current_sum += nums[i]
        
    average = current_sum / k
    
    for i in range(k, n):
        current_sum += nums[i]
        current_sum -= nums[i-k]
        new_avg = current_sum/k
        average = max(average, new_avg)
    
    return average

nums = [1,12,-5,-6,50,3]
k = 4

print(maximum_average_subarray(nums, k))"""


# Another Solution using sliding window after learning Queue

def maximum_average_subarray(nums, k):
    if k <= 0 or k > len(nums):
        return None

    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i]
        window_sum -= nums[i-k]

        max_sum = max(max_sum, window_sum)

    return max_sum / k

nums = [1,12,-5,-6,50,3]
k = 4

print(maximum_average_subarray(nums, k))