# Challenge 1 — Maximum Sum of Size K

def max_sum_subarray(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for right in range(k, len(nums)):
        window_sum += nums[right]
        window_sum -= nums[right-k]
        max_sum = max(max_sum, window_sum)

    return max_sum

nums = [2, 1, 5, 1, 3, 2]
k = 3

print(max_sum_subarray(nums, k))

# Challenge 2 — Minimum Sum of Size K

def min_sum_subarray(nums, k):
    window_sum = sum(nums[:k])
    min_sum = window_sum

    for right in range(k, len(nums)):
        window_sum += nums[right]
        window_sum -= nums[right-k]
        min_sum = min(min_sum, window_sum)

    return min_sum

nums = [2, 3, 1, 5, 6, 2]
k = 3

print(min_sum_subarray(nums, k))

# Challenge 3 — Maximum Number of 1s in a Window

def max_ones(nums, k):
    current_one = 0

    for i in range(k):
        current_one += nums[i]

    max_one = current_one

    for i in range(k, len(nums)):
        current_one += nums[i]
        current_one -= nums[i-k]

        max_one = max(max_one, current_one)
    
    return max_one

nums = [1, 0, 1, 1, 0, 1, 0, 1]
k = 3

print(max_ones(nums, k))

# Challenge 4 — Minimum Size Subarray

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

    if answer == float("inf"):
        return 0
    
    return answer

target = 15
nums = [1, 2, 3, 5, 7, 2]

print(min_subarray_len(target, nums))

# Challenge 5 — Maximum Average

def max_average(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for right in range(k, len(nums)):
        window_sum += nums[right]
        window_sum -= nums[right-k]
        max_sum = max(max_sum, window_sum)

    return max_sum/k

nums = [1, 12, -5, -6, 50, 3]
k = 4

print(max_average(nums, k))

# Challenge — Longest Subarray With Sum ≤ Target

def longest_subarray(nums, target):
    left = 0
    window_sum = 0
    answer = 0

    for right in range(len(nums)):
        window_sum += nums[right]

        while window_sum > target:
            window_sum -= nums[left]
            left += 1

        answer = max(answer, right - left + 1)

    return answer

nums = [1, 2, 1, 0, 1, 1, 0]
target = 4

print(longest_subarray(nums, target))

# Challenge — Longest Substring Without Repeating Characters

def longest_unique_substring(s):
    left = 0
    answer = 0
    seen = set()

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])

        answer = max(
            answer,
            right - left + 1
        )

    return answer

s = "pwwkew"
print(longest_unique_substring(s))