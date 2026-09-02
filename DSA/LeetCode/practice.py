def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:

        mid = (left + right) // 2

        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def find_first_occurrence(nums, target):
    left = 0
    right = len(nums) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if target == nums[mid]:
            result = mid
            right = mid - 1
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return result


def find_last_occurrence(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:

        mid = (left + right) // 2

        if target == nums[mid]:
            left = mid + 1
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1

    return right


nums = [1, 2, 2, 2, 3, 4, 5]

print(binary_search(nums, 2))
print(find_first_occurrence(nums, 2))
print(find_last_occurrence(nums, 2))