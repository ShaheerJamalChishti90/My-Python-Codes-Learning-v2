# if 3 == True + 2:
#     print("Equal")
# else:
#     print("Not equal to 3")
 
# a = True + 5
# print(a)


# class Person:
#     def __init__(self):
#         self.__name = 'Shaheer'

# person = Person()
# print(person._Person__name)

# from tkinter.tix import InputOnly


def mimi(n):
    if n == 1:
        return 1
    else:
        return n * mimi(n-1)
    
number = int(input("Enter a number: "))
print(mimi(number))