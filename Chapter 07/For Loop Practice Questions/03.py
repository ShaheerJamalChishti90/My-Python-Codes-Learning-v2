# Factorial: Write a program that calculates the factorial of a number using a for loop. For example, factorial of 5 is 5 × 4 × 3 × 2 × 1.

n = int(input("number here: "))

for i in range(1, n):
    n*=i # 5 = 5 * 1
    i += 1 # i = i + 1
print(n)

'''

OUTPUT:
number: 5
1-5

n = n * i
i = i + 1

5 = 5 x 1 => 5
i = 1 + 1 => 2

5 = 5 x 2 => 10
i = 2 + 1 => 3

10 = 10 x 3 => 30 
i = 3 + 1 => 4

n = 30 x 4 => 120
i = 4 + 1 => 5


'''