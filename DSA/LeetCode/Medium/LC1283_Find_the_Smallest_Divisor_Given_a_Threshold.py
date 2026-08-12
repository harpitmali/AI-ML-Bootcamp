def smallest_divisor(nums, threshold):
    left = 1
    right = max(nums)

    while left <= right:
        mid = (left + right) // 2

        total = 0
        for num in nums:
            total += (num + mid - 1) // mid

        if total <= threshold:
            right = mid - 1
        else:
            left = mid + 1

    return left


nums = [21212,10101,12121]
threshold = 1000000

print(smallest_divisor(nums, threshold))
