# Do practice of menue driven program. Like 1 for add , 2 for exit

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    else:
        return a / b

def calculator():
    while True:
        print("Menu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
            
        choice = input("Enter your choice (1-5): ")
        if choice == '5':   
            print("Exiting the calculator.")
            break
        if choice in ['1', '2', '3', '4']:
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue
                
            if choice == '1':
                result = add(a, b)
                print(f"The result of addition is: {result}")
            elif choice == '2':
                result = subtract(a, b)
                print(f"The result of subtraction is: {result}")
            elif choice == '3':
                result = multiply(a, b)
                print(f"The result of multiplication is: {result}")
            elif choice == '4':
                result = divide(a, b)
                print(f"The result of division is: {result}")
            else:
                print("Invalid choice. Please try again.")
                    
calculator()









  