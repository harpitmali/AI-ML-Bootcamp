import math

""" x = 10

# x = x + 1
# x += 1

# x = x - 2
# x -= 2

# x = x * 2
# x *= 2

# x = x / 5
# x /= 5

# x = x**2
# x **= 2

# rem = x % 2
# rem %= 2

print(x) """



""" a = 3.14
b = -4
c = 5

result =  round(a)
# result = abs(b)
# result = pow(4, 3)
# result = max(a, b, c)
# result = min(a, b, c)

print(result) """



# print(math.pi)
# print(math.e)

# x = 9.1 

# result = math.sqrt(x)
# result = math.ceil(x) always round number up
# result = math.floor(x) # always round number down

# print(x)


""" # Excersice 1 Calculate  C = 2(Pi)r

radius = float(input("Enter the radius of a Circle: "))

result = 2 * (math.pi) * radius

print(f"The Circumference = {round(result, 2)}cm") """



""" # Exersice 2 Calculate Area of the Circle

radius = float(input("Enter the radius of a Circle: "))

area = math.pi * math.pow(radius, 2)

print(f"Area of the Circle is : {round(area, 2)}cm^2") """

# Exersice 3 Calculate Side of the triangle

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"C = {round(c, 2)}cm")