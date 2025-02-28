# 5. Write a program to find the maximum of the numbers
# in a list using the reduce function.


from functools import reduce
ls = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]

# max = reduce(max, ls)
# print(max) #Output: 70

def greater(x, y):
    if x > y:
        return x
    else:
        return y
print(reduce(greater, ls)) #Output: 70


# def add(x, y):
#     return x + y
# print(reduce(add, ls)) 