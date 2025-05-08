#Core Concept:
    # 1. How many rows? --> Outter loop
    # 2. What to print inside each row? --> Inner loop

import numbers


for row in range(1, 5):
    for star in range(row):
        print("* ", end="")
    print()  



# * * *
# * * *
# * * *
for rows in range(1, 4):
    for stars in range(1, 4):
        print("* ", end="")
    print()



# 1 2 3
# 4 5 6
# 7 8 9

for rows in range(1, 4):
    for elements in range(1, 4):
        print((rows - 1) * 3 + elements, end=" ")  
    print()