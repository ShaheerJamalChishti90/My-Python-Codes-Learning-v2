# Write a program to find whether a given number is prime or not.

# n = int(input("number: "))
# for i in range(2, n):
#     if (n % i) == 0:
#         print(f"{n} is not a prime number")
#         break
#     else:
#         print(f"{n} is a prime number")
#         break

# ABOVE CODE IS WRONG: https://chatgpt.com/share/438d5451-cca6-4350-aa15-a7bbf577f489
# CORRECTED CODE IS IN THE LINK TO CHAT-GPT
# CORRECTED CODE IS BELOW:

n = int(input("number: "))

if n < 2:
    print(f"{n} is not a prime number")
else:
    for i in range(2, n):
        if (n % i) == 0:
            print(f"{n} is not a prime number")
            break
    else:
        print(f"{n} is a prime number")

# Write a Python program to print all prime numbers between two given numbers.

# Take input for the start and end of the range
number1 = int(input("Enter the start of the range: "))
number2 = int(input("Enter the end of the range: "))

if number1 < 2 or number2 < 2:
    print("The number is below 2, invalid input for checking prime numbers")
else:
    print(f"Prime numbers between {number1} and {number2}:")
    for num in range(number1, number2 + 1):
        if num > 1:  # Only check numbers greater than 1

            is_prime = True  # Assume the number is prime
            
            # Check divisibility from 2 to num-1
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False  # Not a prime number
                    break  # No need to check further
            if is_prime:
                print(num, end=" ")
    print()  # Move to the next line after printing all primes






