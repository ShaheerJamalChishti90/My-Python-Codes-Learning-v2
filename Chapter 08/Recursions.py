# # Calculating factorial using formula (n-1)

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n-1)


# n = int(input("Enter number here: "))
# print(f'The factorial of {n} is {factorial(n)}')



# n = int(input("Number: "))

# for i in range(1, n):
#     n = n * i
#     i = i + 1
#     print(f'The factorial of {i} is {n}')

# Q02: Printing numbers backward till 0:

# a = int(input("Number: "))
# def count_down(a):
#     if a <= 0:  # This is where the counting stops
#         print("Done!")
#     else:
#         print(a)  # Counter says the current number
#         count_down(a - 1)  # Counter asks another Counter to count down the next number
# count_down(a)

# Q02: Printing the same code using for loop:

# for i in range(a, 0, -1):
#     print(i)
#     print("Done!")
   
   
   
# Understanding Recursions:

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
    
# '''
#     n = 5
#     n * factorial(n-1)

#     5 * factorial(5-1)
#     5 * 4 * factorial(4-1))
#     5  * 4 * 3 * factorial(3-1))
#     5 * 4 * 3 * 2 * factorial(2-1)
#     5 * 4 * 3 * 2 * 1 

# '''    
    
# n = int(input('enter number here: '))     
# print(f'The factorial of {n} is {factorial(n)}')

# Quick Quix: Fibonacci Series;

# def fibonacci(n):
#     # Base case: the first and second numbers of the Fibonacci sequence are 0 and 1
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     # Recursive case: sum of the two preceding numbers
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)

# # Test the function with an example
# num = int(input('number: '))

# print(f"Fibonacci sequence up to {num}:")
# for i in range(num):
#     print(fibonacci(i))


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input('Number here: '))

print(f'The sequence from {n} goes like Booom!!')
for i in range(n):
    print(fibonacci(i))
