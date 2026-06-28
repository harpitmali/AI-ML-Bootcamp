# Assignment 1 — Calculator

def add(a, b):
    return a+b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by 0"
    return a / b

a = int(input("Enter a Number : "))
b = int(input("Enter another number : "))

while True:
    choose = input("What would like to do (+, -, *, /) : ")

    if choose ==  "+":
        print(add(a, b))
        break
    elif choose == "-":
        print(subtract(a, b))
        break
    elif choose == "*":
        print(multiply(a, b))
        break
    elif choose == "/":
        print(divide(a,b))
        break
    else:
        print("Wrong Input")
        print("Try again")


# Assignment 2 — Maximum of Three Numbers

def maximum(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    elif a == b and a > c:
        print("A and B are Equal")
        return a
    elif a == c and a > b:
        print("A and C are Equal")
        return a
    elif b == c and b > a:
        print("B and C are Equal")
        return b
    elif a == b == c:
        print("A == B == C")
        return a

a = int(input("Enter A = "))
b = int(input("Enter B = "))
c = int(input("Enter C = "))

print(maximum(a, b, c))



# Assignment 3 — Prime Number Checker

def is_prime(num):
    if num == 0 or num == 1:
        return False
    
    for i in range(num-1, 1, -1):
        if num % i == 0:
            return False
        
    return True

num = int(input("Enter a number: "))

print(is_prime(num))

# Assignment 4 — Fibonacci

def fibonacci(n):
    a = 0
    b  = 1
    if n == 0:
        print("First n number need to be above 0")
    else: 
        for i in range(n):
            print(a)
            a, b = b, a+b

num = int(input("Enter a number: "))

fibonacci(num)


# Bonus Challenge — Statistics Function

def statistics(*numbers):
    total = 0
    maximum = numbers[0]
    for i in range(len(numbers)):
        total += numbers[i]
        if maximum < numbers[i]:
            maximum = numbers[i]
    
    average = total / len(numbers)
    return total, average, maximum


total, average, maximum = statistics(10,20,30)
print(f"Sum : {total}")
print(f"Average : {average}")
print(f"Maximum : {maximum}")