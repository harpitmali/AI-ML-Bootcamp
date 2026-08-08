def find_first(nums, target):
    left = 0
    right = len(nums) - 1
    answer = -1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            answer = mid
            right = mid - 1
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return answer

def find_last(nums, target):
    left = 0
    right = len(nums) - 1
    answer = -1

    while left <= right:
        mid = (left + right) // 2

        if target == nums[mid]:
            answer = mid
            left = mid + 1
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return answer

def search_range(nums, target):
    first = find_first(nums, target)
    last = find_last(nums, target)

    return [first, last]

nums = [5, 7, 7, 8, 8, 10]
target = 6

print(search_range(nums, target))