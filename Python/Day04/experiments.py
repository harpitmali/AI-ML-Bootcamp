# Experiment 1 — While Loop

count = 1

while count <= 5:
    print(count)
    count += 1

# Experiment 2 — break
count = 1    

while True:
    print(count)

    if count == 5:
        break

    count += 1

# Experiment 3 — continue

for i in range(1, 11):
    if i == 5:
        continue
    
    print(i)

# Experiment 4 — Nested Loop
    
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()

# Experiment 5 — Bonus

for i in range(3):
    print(i)

print("Done")

