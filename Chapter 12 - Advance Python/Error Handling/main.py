x = input("Enter your first number here: ")
y = input("Enter your second number here: ")


def calculator():
    try:
        x_int = int(x)
        y_int = int(y)
        
        result = x_int / y_int 

    except ZeroDivisionError as ze:
        print(f"Sorry Sir, Division is not allowed by Zero! {ze}")

    except ValueError as ve:
        print(f"Sorry Sir, Invalid Input! Only integers are allowed: {ve}")

    except Exception as e:
        print(f"An error occurred: {e}")

    else:
        print(f"The result is: {int(result)}")
    
    print("Thank you for using our calculator!")

calculator()