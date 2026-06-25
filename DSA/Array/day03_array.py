# Insert at End -> in this program we will insert a new element at the end of the array
def insert_end(arr, value):
    arr.append(value)
    return arr

# Insert at Beginning -> move everything one step forward and store new value at starting
def insert_beginning(arr, value):
    new_arr = [0] * (len(arr) + 1)
    new_arr[0] = value
    for i in range(len(arr)):
        new_arr[i+1] = arr[i]
    return new_arr

# Insert at Index -> store at given index and move elements from given index one step forward
def insert_at_index(arr, index, value):
    new_arr = []
    for i in range(index):
        new_arr.append(arr[i])
    
    new_arr.append(value)

    for i in range(index, len(arr)):
        new_arr.append(arr[i])
    return new_arr

# Delete by Value -> delete element and adjust array move everything after that one down 
def delete_element(arr, value):
    for i in range(len(arr)):
        if arr[i] == value:
            for j in range(i, len(arr)-1):
                arr[j] = arr[j+1]
            arr.pop()
            return arr

    return -1

# Delete by Index -> deleting element by index then shifting everythig backword
def delete_index(arr, index):
    if index < 0 or index >= len(arr):
        return arr
    
    for i in range(index, len(arr)-1):
        arr[i] = arr[i+1]
    arr.pop()
    return arr

arr = [10, 20, 30]
print(insert_end(arr, 40))

arr = [10, 20, 30]
print(insert_beginning(arr, 40))

arr = [10, 20, 30]
print(insert_at_index(arr, 1, 40))

arr = [10, 20, 30 ,40]
print(delete_element(arr, 30))

arr = [10, 20, 30 ,40]
print(delete_index(arr, 1))