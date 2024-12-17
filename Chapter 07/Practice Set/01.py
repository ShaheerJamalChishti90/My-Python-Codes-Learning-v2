# Write a program to print multiplication table of a given number using for loop.


number = int(input("Enter any number here: "))

# for i in range(1, 11):
#     print(f"{number} * {i} = {number * i}")  # f-string

i = 1

while i <= 10:
    print(f"{number} * {i} = {number * i}")
    i = i + 1