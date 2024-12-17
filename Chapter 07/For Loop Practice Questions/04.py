# List Average: Given a list of numbers, write a program that calculates and prints the average of the numbers using a for loop.

nl = [5, 10, 15, 20]
sum = 0

for i in nl:
    # avg = sum/total
    sum = sum + i
print(sum/len(nl))