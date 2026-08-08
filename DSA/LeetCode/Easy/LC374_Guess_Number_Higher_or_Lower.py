def guessNumber(n):
    left = 0
    right = n

    while left <= right:
        mid = (left + right) // 2

        if guess(mid) == 0:
            return mid
        elif guess(mid) == 1:
            left = mid + 1
        else:
            right = mid - 1

def guess(num):
    if num == pick:
        return 0
    elif num < pick:
        return 1
    else:
        return -1
        
pick = 1

print(guessNumber(10))