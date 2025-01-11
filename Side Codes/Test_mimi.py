# What is the result of the following code?

# a = [1, 2] #list 
# b = ['a', 'b', 'c'] #list

a = ["Shaheer", "Mirani"]
b = [22, 20]
c = list(zip(a, b))

# print(list(c))
# print(c)
for a, b in c:
    print(f'{a} is {b} years old!')