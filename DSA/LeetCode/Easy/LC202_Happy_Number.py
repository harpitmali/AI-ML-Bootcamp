def is_Happy(num):
    seen = set()


    while num != 1:

        if num in seen:
            return False
        
        seen.add(num)
        num = get_next_number(num)
    
    return True
        

def get_next_number(num):
    total = 0

    while num > 0:
        digit = num % 10
        total += digit * digit
        num //= 10

    return total
        

num = 20
print(is_Happy(num))
