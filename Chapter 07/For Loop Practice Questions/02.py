# Multiplication Table: Create a Python program that prints the multiplication table for any number provided by the user (e.g., table of 5).

n = int(input("Enter any number here: "))

for i in range(1, 11):
    table = n * i
    print(f'{n} x {i} = {table}')