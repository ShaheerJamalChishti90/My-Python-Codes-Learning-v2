# Write a recursive function to find the factorial of a number. The factorial of a number n is the product of all integers from 1 to n.

def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
    
'''
    n = 5
    n * factorial(n-1)

    5 * factorial(5-1)
    5 * 4 * factorial(4-1)
    5 * 4 * 3 * factorial(3-1)
    5 * 4 * 3 * 2 * factorial(2-1)
    5 * 4 * 3 * 2 * 1 

'''
    
    
    
    
    
    
    
    
    
n = int(input('number here: '))
print(f'The factorial of {n} is {factorial(n)}')