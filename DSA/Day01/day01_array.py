def find_max(arr):
    x = arr[0]
    for i in range(len(arr)):
        if x < arr[i]:
            x = arr[i]
    print(f"Maximum :{x}")

def find_min(arr):
    x = arr[0]
    for i in range(len(arr)):
        if x > arr[i]:
            x = arr[i]
    print(f"Minimum :{x}")

def sum_of_array(arr):
    total = 0
    for i in range(len(arr)):
        total = total + arr[i]
    print(f"Sum of array : {total}")

def count_of_even(arr):
    even = 0
    for i in range(len(arr)):
        if arr[i]%2 == 0:
            even += 1
    print(f"No of even no is : {even}")

def count_of_odd(arr):
    odd = 0
    for i in range(len(arr)):
        if arr[i]%2 != 0:
            odd += 1
    print(f"No of odd no is : {odd}")

def reverse_array(arr):
    x1 = []
    for i in range(len(arr)-1, -1, -1):
        x1.append(arr[i])
    return x1
        

arr = [-3, 8, 0, 15]
find_max(arr)
find_min(arr)
sum_of_array(arr)
count_of_even(arr)
count_of_odd(arr)
print(reverse_array(arr))