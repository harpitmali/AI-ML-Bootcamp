def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low+high) // 2

        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1


    return -1


arr = [2,5,8,12,16,23,38,56,72]

print(binary_search(arr, 23))   # 5
print(binary_search(arr, 2))    # 0
print(binary_search(arr, 72))   # 8
print(binary_search(arr, 100))  # -1