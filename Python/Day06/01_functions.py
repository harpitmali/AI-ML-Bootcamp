# function() = A block of reusable code
#              place () after function name to invoke it



def happy_birthday(name, age):
    print(f"Happy Birthday {name}!")
    print(f"You are {age} years old")
    print("Happy Birthday to you!")

happy_birthday("Harpit", 21)



def invoice_display(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")


invoice_display("Harpit", 99.99, "01/06")

# return = statement used to end the function
#          and send a retult back to caller

def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def division(x, y):
    z = x / y
    return z

print(add(5,3))
print(subtract(5,3))
print(multiply(5,3))
print(division(5,3))



def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("harpit", "mali")
print(full_name)

def add(a,b):
    print(a+b)

result = add(2,3)
print(result)