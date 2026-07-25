def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        
    return -1

def find_second_largest(arr):
    largest = arr[0]
    second_largest = arr[1]

    if second_largest > largest:
        temp = second_largest
        second_largest = largest
        largest = temp

    for num in arr[2:]:
        if num > largest:
            second_largest = largest
            largest = num
        elif num != largest and (second_largest == largest or num > second_largest):
            second_largest = num

    return second_largest 


def count_positive(arr):
    total = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            total += 1
    
    return total

def count_negative(arr):
    total = 0
    for i in range(len(arr)):
        if arr[i] < 0:
            total += 1
    
    return total

def average_array(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i]

    average = total / len(arr)
    return average

arr = [20, 5, 10, 15]
target = 5
print(linear_search(arr, target))

second_largest = find_second_largest(arr)
print(f"Second largest value in arr is {second_largest}")

positive_count = count_positive(arr)
print(f"Positive number count: {positive_count}")

negative_count = count_negative(arr)
print(f"Negative number count: {negative_count}")

average = average_array(arr)
print(f"Average: {average}")