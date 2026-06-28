# *args = allows you pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword arguments
#            * unpacking operator
#           1. Positional, 2. default, 3. keyword, 4. arbitrary


def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1,2,3,4,5))


def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Mali", "Harpit", "Rajeshkumar")
print()


def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="123 Fake st.", 
              city="Deesa", 
              state="Gujarat", 
              zip="1234")


def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()

    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("Mali", "Harpit", "Rajeshkumar",
               street="123 Fake st.", 
               city="Deesa", 
               state="Gujarat", 
               zip="1234"
              )