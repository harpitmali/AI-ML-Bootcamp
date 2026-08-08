def mySqrt(x):
    left = 0
    right = x
    answer = 0

    while left <= right:
        mid = (left + right) // 2

        if (mid * mid) == x:
            return mid
        elif (mid * mid) < x:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer

print(mySqrt(4))    # 2
print(mySqrt(8))    # 2
print(mySqrt(16))   # 4
print(mySqrt(1))    # 1
print(mySqrt(0))    # 0
print(mySqrt(25))   # 5
print(mySqrt(26))   # 5