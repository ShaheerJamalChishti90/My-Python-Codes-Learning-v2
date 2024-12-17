# Write a python function to print first n lines of the following pattern:

# ***
# ** - for n = 3
# *


def stars(n):
    a = "*"
    for i in range(n, 0, -1):
        print(a * i)
n = int(input('Enter any number here: '))
stars(n)