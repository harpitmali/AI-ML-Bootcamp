def min_subarray_len(target, nums):
    left = 0
    window_sum = 0
    answer = float("inf")

    for right in range(len(nums)):
        window_sum += nums[right]
        while window_sum >= target:
            answer = min(answer, right - left + 1)
            window_sum -= nums[left]
            left += 1

    return answer


target = 7
nums = [2, 3, 1, 2, 4, 3]

print(min_subarray_len(target, nums))