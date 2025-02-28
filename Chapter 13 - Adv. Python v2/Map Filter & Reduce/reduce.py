# Reduce applies a rolling computation to sequential pair of elements.

# value = reduce(function, list1) 
from functools import reduce

# def add(x, y):
#     return x + y

def square(x, y):
    return x * y

# ls = [2, 4, 6, 8, 10] #2+4=6, 6+6=12, 12+8=20, 20+10=30
ls = [2, 4, 6] 
# result = reduce(add, ls)
result = reduce(square, ls)
print(result)  # Output: 30

#reduce func pehle 2 elements pe apply hota hai,
# phir uska output agli element ke sath add hota hai
# aurr ye iss hii tarhan chalta hai last element tak.