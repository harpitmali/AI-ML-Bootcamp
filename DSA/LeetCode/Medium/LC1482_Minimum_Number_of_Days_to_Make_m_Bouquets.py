def min_days(bloomDay, m, k):

    if m * k > len(bloomDay):
        return -1

    left = min(bloomDay)
    right = max(bloomDay)

    while left <= right:

        mid = (left + right) // 2

        flowers = 0
        bouquest = 0
        for bloom in bloomDay:
            if bloom <= mid:
                flowers += 1
                if flowers == k:
                    bouquest += 1
                    flowers = 0
            else:
                flowers = 0

        if bouquest >= m:
            right = mid - 1
        else:
            left = mid + 1

    return left

bloomDay = [1,10,3,10,2]
m = 3
k = 1

print(min_days(bloomDay, m, k))