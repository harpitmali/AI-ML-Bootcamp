def contains_duplicate(nums):
    seen = set()

    for i, num in enumerate(nums):

        if num in seen:
            return True
        
        seen.add(num)

    return False

nums = [1,1,1,3,3,4,3,2,4,2]

print(contains_duplicate(nums))