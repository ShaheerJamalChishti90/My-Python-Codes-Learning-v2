#Q1: Print a square pattern made of stars
# *****
# *****
# *****

for rows in range(3):
    for stars in range(3):
        print("*", end="  ")
    print()
    
print("-----")
    
# *
# ***
# *****
a = "*"
for rows in range(1, 4):
    for stars in range(rows):
        print(a, end=" ")
    print()
    
