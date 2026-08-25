def subarrays_with_k_distinct(nums, k):

    def at_most(k):
        left = 0
        count = {}
        result = 0

        for right in range(len(nums)):

            count[nums[right]] = count.get(nums[right], 0) + 1

            while len(count) > k:
                count[nums[left]] -= 1

                if count[nums[left]] == 0:
                    del count[nums[left]]

                left += 1

            result += right - left + 1

        return result

    return at_most(k) - at_most(k - 1)

nums = [1, 2, 1, 2, 3]
k = 2

answer = subarrays_with_k_distinct(nums, k)

print(answer)