def two_sum(nums, target):
    my_dict = {}

    for i, nums in enumerate(nums):
        need = target - nums
        
        if need in my_dict:
            return [my_dict[need], i]
        
        my_dict[nums] = i
        
    return []


nums = [2, 7, 11, 15]
target = 9

print(two_sum(nums, target))