# Write a Python program to print all numbers from 1 to 10 using a for loop.
for i in range(1, 11):
    print(i)

# Write a program that calculates the sum of all numbers from 1 to 100 using a for loop.
s = 0 
for i in range(1, 101):
    s += i  # s = s + i
print(s)

# Write a program that prints numbers from 10 to 1 in descending order using a for loop.
for i in range(10, 0, -1):
    print(i)
    
# Write a program to calculate the factorial of a number entered by the user using a for loop.
# (Factorial of n is the product of all positive integers less than or equal to n.)
n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i  # factorial = factorial * i
print(f"Factorial of{n} is {factorial}")

# Write a program that prints a pattern of asterisks (*) 
# in the shape of a right-angled triangle.
# The number of rows should be determined by the user input.


# Print all even numbers from 1 to 50.
# Hint: Use a for loop and the modulus operator (%).
for i in range(1, 51):
    if i % 2 == 0:  
        print(i)  

# Calculate and print the sum of all odd numbers between 1 and 100.
# Hint: Use a for loop and an if condition inside it.
odd_n = 0
for i in range(1, 101):
    if i % 2 != 0:  
        odd_n += i 
print(f"Sum of odd numbers between 1 and 100 is {odd_n}")

# Ask the user to enter a word and count how many vowels are in that word using a for loop.
# Hint: Loop through each character in the string
word = input("Enter a word: ")
vowels = "aeiouAEIOU"
count = 0
for char in word:
    if char in vowels:
        count += 1
print(f"The number of vowels in '{word}' is {count}")

# Find and print all prime numbers between 1 and 100.
# Hint: For each number, check how many times it is divisible — use a for loop inside the main one 
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

for num in range(1, 101):
    if is_prime(num):
        print(num)
        
# Ask the user for 10 numbers and count how many of them are positive, negative, and zero. Print the result.
# Hint: Loop 10 times and use if-elif-else to classify each number.

user_input = []
positive_count = 0
negative_count = 0 
zero_count = 0

for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    user_input.append(num)
    
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1