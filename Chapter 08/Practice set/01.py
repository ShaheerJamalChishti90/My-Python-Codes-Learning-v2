# Write a program using functions to find greatest of three numbers



def greatest_number():
    a = int(input("Number: "))
    b = int(input("Number: "))
    c = int(input("Number: "))
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

gr_num = f'The greatest number is {greatest_number()}'  
print(gr_num)  

