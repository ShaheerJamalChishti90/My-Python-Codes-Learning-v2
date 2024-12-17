# Even Numbers: Write a program that prints all the even numbers between 1 and 50 using a for loop.

for i in range(0, 50, 2):
    print(i)


for i in range(0, 51):
    if i%2 == 0 or i%2 == i:
        print(f'{i} is an even number') 
    else:
        print("")
        print(f'{i} is an odd number')  
