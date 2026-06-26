# for loop -> Execute a block of code fixed number of times
#             we can iterate through range, string, squence etc..

for x in range(1, 11):
   print(x)

for x in reversed(range(1,11)):
    print(x)

print("Happy New Year")


credit_card = "1234-5678-9012-3456"

for x in credit_card:
    print(x)

for i in range(1, 11):
    if i == 7:
        continue
    else:
        print(i)

for i in range(1, 11):
    if i == 4:
        break
    else:
        print(i)