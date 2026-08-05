def contains_nearby_duplicate(nums, k):
    window = set()

    for i in range(len(nums)):
        if nums[i] in window:
            return True
        
        window.add(nums[i])

        if i >= k:
            window.remove(nums[i-k])

    return False


nums = [1,2,3,1]
k = 3

print(contains_nearby_duplicate(nums, k))