def calculator():
    print("Welcome to the calculator")
    print("Please enter the first number")
    num1 = int(input())
    print("Please enter the second number")
    num2 = int(input())
    print("Please enter the operation you want to perform")
    operation = input()
    if operation == "+":
        print("The result is: ", num1 + num2)
    elif operation == "-":
        print("The result is: ", num1 - num2)
    elif operation == "*":
        print("The result is: ", num1 * num2)
    elif operation == "/":
        print("The result is: ", num1 / num2)
    else:
        print("Invalid operation")
        
calculator()
