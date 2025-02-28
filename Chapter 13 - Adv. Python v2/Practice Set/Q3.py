# A list contains the multiplication table of 7.
# write a program to convert it to vertical
# string of same numbers.
 
table = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]

#Method 1:
# table = [str(i) for i in table]
# table = "\n".join(table)
# print(table)

#Method 2:
for i in table:
    print(i)