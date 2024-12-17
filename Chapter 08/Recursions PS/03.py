# Write a recursive function that calculates the nth number in the Fibonacci sequence. The Fibonacci sequence is: 0, 1, 1, 2, 3, 5, 8, 13, 21...

# Example: fibonacci(5) should return 5 (since the 5th Fibonacci number is 5)

# https://chatgpt.com/share/b48af32a-680c-4525-887a-d80128dcf7c9

#UPDATED CHAT(CHECK IT OUT MUST!!):  https://chatgpt.com/share/b48af32a-680c-4525-887a-d80128dcf7c9


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
'''
    n = 6
    fibonacci(n-1) + fibonacci(n-2)

    6-1 + 6-2
    5 + 4 = 9
    
'''
n = int(input('Number here: '))
print(fibonacci(n))