# default arguments = A default value for certain paramenters
#                     default is used when that argument is omitted
#                     make your function more flexible, reduces number of arguments
#                     1. Positional, 2. default, 3. keyword, 4. arbitrary


def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500))
print(net_price(500, 0.1))
print(net_price(500, 0.05, 0))


import time

def count(end, start=1):
    for i in range(start, end+1):
        print(i)
        time.sleep(1)

# count(10)
count(5, 0)