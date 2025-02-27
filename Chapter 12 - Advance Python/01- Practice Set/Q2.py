# 2. Write a program to print third, fifth and seventh element from a list using enumerate
# function.


ls = [160, 165, 170, 175, 180, 185, 190, 195, 200]
item = 1

for x, y in enumerate(ls):
    if x == 2 or x == 4 or x == 6:
        item += 2
        print(f"The element at index {x} is {y} at item {item}")

# new_ls = [item for index, item in enumerate(ls) if index == 2 or index == 4 or index == 6 ] 
# print(new_ls)