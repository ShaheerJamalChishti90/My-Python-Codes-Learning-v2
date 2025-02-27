# 4. Write a program to display a/b where a and b are integers. If b=0, display infinite by
# handling the ‘ZeroDivisionError’.

from multiprocessing import Value


a = input("Enter the value of a: ")
b = input("Enter the value of b: ")

try:
    print('Here we performs the division of a and b')
    division = int(a) / int(b)

except ZeroDivisionError as ze:
    print(f"Error: It seems like you try to divide by 0; {ze} - Division by zero is not possible, Its infinity!!")

except ValueError as ve:
    print(f"Error: It seems like you are trying to enter something abnormal; {ve} - Only numbers are allowed. Please enter a valid number.")

except Exception as e:
    print(f"Error: Are you fucking dumb? who enters that value; {e} - Something went wrong.")
    
else:
    print(f"The division of a and b is {division}")
    
finally:
    print("Thanks for using our software.")