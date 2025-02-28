  #lambda  arguments:  expression 
    # |      |            |
# a = lambda x = 1, y = 2: x + y
# print(a())


def square(x):
    print(x**2)

a = int(input("Enter a number: "))
square(a)

sqr = lambda x: x * x
print(sqr(5))