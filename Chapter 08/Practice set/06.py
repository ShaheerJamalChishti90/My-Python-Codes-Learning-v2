# Write a python function to print multiplication table of a given number

def table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
        
n = int(input("Enter a number here: "))
table(n)  # call the function with the input number