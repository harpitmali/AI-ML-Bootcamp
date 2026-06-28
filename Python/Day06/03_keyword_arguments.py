# keyword arguments = an argument preceded by identifier
#                     helps with readability
#                     order of argument doesn't matter
#                     1. Positional, 2. default, 3. keyword, 4. arbitrary


def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

hello("Hello", last="Mali", first= "Harpit", title="Mr.")


for i in range(6):
    print(i, end=" ")

print()

print("1", "2", "3", "4", "5", sep="-")

def get_phone(country, area, first, last):
    return f"+{country} {area}{first}{last}"

phone_num = get_phone(country=91, area=123, first=456, last=7890)
print(phone_num)