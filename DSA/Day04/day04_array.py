# Linear Search -> We are going to look at every value in array when we match value with array then we return index

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        
    return -1

arr = [10, 20, 30, 40, 50]

print(linear_search(arr, 50))
    

# Count Frequency -> We have a targeted value we run the loop when we see same value as targeted value then we increase the count an at the end we return count

def count_frequency(arr, target):
    count = 0
    for i in arr:
        if i == target:
            count += 1
        
    return count

arr = [10, 20, 20, 30, 40, 20]
print(count_frequency(arr, 20))

# Find First Occurrence -> We run the loop when we see the first value as same as teargeted value then we break the loop and return that index

def first_occurrence(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        
    return -1

arr = [10, 20, 20, 30, 40, 20]
print(first_occurrence(arr, 20))

# Find Last Occurrence -> we run the loop when we see value same as targeted value then we store the index in variable and after whole loop finish running we return that variable

def last_occurrence(arr, target):
    index = -1
    for i in range(len(arr)):
        if arr[i] == target:
            index = i
        
    return index

arr = [10, 20, 30, 20, 50, 20]
print(last_occurrence(arr, 20))

# Bonus 1 — Transposition Search

def linear_search_transposition(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            if i == 0:
                return i
            else:
                temp = arr[i]
                arr[i] = arr[i-1]
                arr[i-1] = temp
                return (i-1)
    return -1

arr = [5,8,2,9,1]
print(linear_search_transposition(arr, 9))

# Bonus 2 — Move-to-Front Search

def linear_search_move_to_front(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            if i == 0:
                return 0
            
            temp = arr[i]
            for j in range(len(arr)):
                arr[j] = arr[j-1]

            arr[0] = temp
            return 0
                
    return -1        
    
arr = [5,8,2,9,1]
print(linear_search_move_to_front(arr, 9))