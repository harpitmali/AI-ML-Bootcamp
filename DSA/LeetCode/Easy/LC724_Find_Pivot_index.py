def find_pivot_index(nums):
    total_sum = 0
    left_sum = 0
    for i in range(len(nums)):
        total_sum += nums[i]

    for i in range(len(nums)):
        right_sum = total_sum - left_sum - nums[i]
        if right_sum == left_sum:
            return i

        left_sum += nums[i]

    return -1

nums = [1, 7, 3, 6, 5, 6]

print(find_pivot_index(nums))