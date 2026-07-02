# LeetCode #26 - Remove Duplicates from Sorted Array

# Topic:
# Two Pointers

# Time Complexity:
# O(n)

# Space Complexity:
# O(1)


def remove_duplicate_from_sorted_array(nums):
    i = 0

    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    
    return nums[:i+1]

nums = [0,0,1,1,1,2,2,3,3,4]
print(remove_duplicate_from_sorted_array(nums))