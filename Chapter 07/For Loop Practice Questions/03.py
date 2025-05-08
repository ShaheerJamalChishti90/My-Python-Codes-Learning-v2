# Factorial: Write a program that calculates the factorial of a number using a for loop. For example, factorial of 5 is 5 × 4 × 3 × 2 × 1.

n = int(input("number here: "))

for i in range(1, n):
    n*=i # 5 = 5 * 1 / n = n * i
    i += 1 # i = i + 1 / i = 1 + 1
print(n)

'''
OUTPUT:
number: 5
1-5

n = n * i
i = i + 1

This is the first iteration of the loop
5 = 5 x 1 => 5 The value of factorial(n) is now updated and is now 5
i = 1 + 1 => 2 Similarly, the value of i is updated to 2

This is the second iteration of the loop
5 = 5 x 2 => 10 Now the new value of factorial is 10
i = 2 + 1 => 3 Similarly, the value of i is updated to 3

This is the third iteration of the loop
10 = 10 x 3 => 30 This time the value of factorial is 30
i = 3 + 1 => 4 and the value of i is updated to 4

This is the fourth and the last iteration of the loop
n = 30 x 4 => 120  #Now the new value of factorial is 120
i = 4 + 1 => 5 and the value of i is updated to 5

The factorial of num is: 120
'''

# num = int(input("Enter a number: "))
# factorial = 1

# if num < 0:
#     print("Factorial is not defined for negative numbers.")
# else:
#     for i in range(1, num + 1):
#         factorial *= i # factorial = factorial * i
#     print("The factorial of", num, "is", factorial)


'''
num = 5
factorial = 1

1 -- 5

#This is the first iteration of the loop
1 = 1 x 1 => 1 #Now the new value of factorial is 1

#Tghis is the second iteration of the loop
2 = 1 x 2 => 2 #Now the new value of factorial is 2

#This is the third iteration of the loop
3 = 2 x 3 => 6 #Now the new value of factorial is 6

#This is the fourth iteration of the loop
4 = 6 x 4 => 24 #Now the new value of factorial is 24

#This is the fifth iteration of the loop
5 = 24 x 5 => 120 #Now the new value of factorial is 120

The factorial of num is: 120
'''


factorial_number = int(input("Enter a number: "))
initial_factorial = 1
# for i in range(1, factorial_number):
#     factorial_number *= i
#     i += 1
# print(f"The factorial is: {factorial_number}")

for i in range(1, factorial_number + 1):
    initial_factorial *= i
print(f"The factorial {factorial_number} is: {initial_factorial}")