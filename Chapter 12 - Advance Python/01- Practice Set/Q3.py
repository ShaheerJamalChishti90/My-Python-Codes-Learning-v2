# 3. Write a list comprehension to print a list which contains the multiplication table of a
# user entered number

x = int(input("Enter the number: "))

# table = [x*i for i in range(1, 11)]
# print(table)

for i in range(1, 11):
    print(f"{x} x {i} = {x*i}")