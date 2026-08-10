def min_eating_speed(piles, h):
    left = 1
    right = max(piles)

    while left <= right:
        mid = (left + right) // 2
        k = mid
        hours = 0
        for pile in piles:
            hours += (pile + k - 1) // k

        if hours <= h:
            right = mid - 1
        else:
            left = mid + 1

    return left

piles = [3, 6, 7, 11]
h = 8

print(min_eating_speed([3, 6, 7, 11], 8))
# 4

print(min_eating_speed([30, 11, 23, 4, 20], 5))
# 30

print(min_eating_speed([30, 11, 23, 4, 20], 6))
# 23