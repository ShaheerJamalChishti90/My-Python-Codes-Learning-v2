# Write a program to find the sum of first n natural numbers using while loop.

n = int(input('number: '))
i = 1
sum = 0 

while i <= n:
    sum = sum + i    # sum += i
    i += 1 # i = i + 1
    
print(sum)

