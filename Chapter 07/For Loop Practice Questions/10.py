# Prime Numbers: Write a Python program to print all prime numbers between 1 and 100 using a for loop.

# prime num, which's divide by 1 and themself and they return the value 0 as a remainder:

# n = int(input("Enter any number here to check if its a prime number or not: "))

for num in range(2, 101):  # Start from 2, since 1 is not a prime number
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)


# Take input from the user
num = int(input("Enter a number: "))

# Assume the number is prime
is_prime = True

# Check if the number is divisible by any number between 2 and num-1
if num > 1:  # Prime numbers are greater than 1
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
else:
    is_prime = False  # Numbers less than or equal to 1 are not prime

# Print the result
if is_prime:
    print(f"{num} is a prime number.")
else:
     print(f"{num} is not a prime number.")

        
n = int(input("enter any number here: "))
prime_hai = True

if n > 1:
    for i in range(2, n):
        if n % i == 0:
            prime_hai = False
            break
else:
    prime_hai = False
    
if prime_hai:
    print(f'{n} is a prime number')
else:
    print(f'{n} is not a prime number')