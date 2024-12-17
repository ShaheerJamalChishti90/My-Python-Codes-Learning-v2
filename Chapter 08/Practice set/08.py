# Write a python function which converts inches to cms

def conversion(n):
    return n * 2.54 

n = int(input("Enter the value here: "))
# def new_func(conversion, n):
#     print(f"{n} in = {conversion(n)} cm")

# new_func(conversion, n)
print(f"{n} in = {conversion(n)} cm")