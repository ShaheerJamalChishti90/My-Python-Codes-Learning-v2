# Do practice of menue driven program. Like 1 for add , 2 for exit

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

user_input = input("Enter your prefrence below:\n1 for addition\n2 for subtraction\n3 for multiplication\n4 to exit: ")

if user_input == '1':
    result = add(x, y)
    print(f"The result of addition is: {result}")
    
elif user_input == '2':
    result = subtract(x, y)
    print(f"The result of subtraction is: {result}")
    
elif user_input == '3':
    result = multiply(x, y)
    print(f"The result of multiplication is: {result}")
elif user_input == '4':
    print("Exiting the calculator.")
else:
    print("Invalid entry. Please try again.")
    