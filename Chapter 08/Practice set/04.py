# Write a recursive function to calculate the sum of first n natural numbers

# a = int(input('Number: '))
# b = int(input('Number: '))
# c = int(input('Number: '))


# def sum():
#     abc = (a+b+c)
#     return abc 

# print(f'The sum of {a}, {b} and {c} is {sum()}')

# ChatGPT corrected code: 
# https://chatgpt.com/share/36e559ff-ec56-4230-bdd4-601b451249aa # Explained Code


def sum_of_natural_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_natural_numbers(n - 1)

# Example usage:
n = int(input("Enter a positive integer: "))
result = sum_of_natural_numbers(n)
print(f"The sum of first {n} natural numbers is: {result}")
