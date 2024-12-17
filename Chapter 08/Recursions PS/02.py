#  Create a recursive function that returns the sum of all numbers from 1 to n.

def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)
    
n = int(input('Number: '))
print(f'The sum of n numbers from {n} to 1 is {sum(n)}')


'''
    n = 5
    return n + sum(n-1)

    5 + sum(5-1)
    5 + 4 + sum(4-1)
    5 + 4 + 3 + sum(3-1)
    5 + 4 + 3 + 2 + sum(2-1)
    5 + 4 + 3 + 2 + 1
    
    
'''