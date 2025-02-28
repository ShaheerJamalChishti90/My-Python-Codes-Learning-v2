# Write a program to filter a list of numbers which are divisible by 5.

ls = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70]

#Method 1:
for i in ls:
    if i%5==0:
        print(i)
        
#Method 2:   
a = filter(lambda a: a%5==0, ls)
print(list(a))
    
