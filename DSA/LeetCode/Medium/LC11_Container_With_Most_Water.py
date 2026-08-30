def maxArea(height):
    left = 0
    right = len(height) - 1
    answer = 0

    while left < right:

        area = (right - left) * min(height[left], height[right])

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

        answer = max(answer, area)

    return answer

height = [1,8,6,2,5,4,8,3,7]

print(maxArea(height))