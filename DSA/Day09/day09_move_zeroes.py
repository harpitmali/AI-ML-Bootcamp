def move_zero(arr):
    left = -1

    for i in range(len(arr)):
        if arr[i] == 0:
            left = i
            break
    
    if left == -1:
        return arr

    for right in range(left+1, len(arr)):
        if arr[right] != 0:
            arr[right], arr[left] = arr[left], arr[right]
            left += 1

    return arr


arr = [0,1,0,3,12]
print(move_zero(arr))