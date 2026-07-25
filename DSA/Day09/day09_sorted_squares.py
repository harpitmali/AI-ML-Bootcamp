def sorted_squares(arr):
    left = 0
    right = len(arr)-1
    result = []

    while left <= right:
        if abs(arr[right]) >= abs(arr[left]):
            result.append(arr[right] ** 2)
            right -= 1
        else:
            result.append(arr[left] ** 2)
            left += 1
    
    result.reverse()
    return result

arr = [-4,-1,0,3,10]
print(sorted_squares(arr))