try : 
    a = int(input("Enter number 1 here: "))
    b = int(input("Enter number 2 here: "))
    result = a/b

    

except ZeroDivisionError as e:
    print(e)
    print("Error: Division by zero is not allowed")
    
except ValueError as e:
    print(e)
    print("Error: Invalid input. Watafak are you trying to do!? Please enter a number.")

except Exception as e:
    print(e)
    print(f"Error: Invalid input :(")

else:
        print(result)

finally:
     print("You going good so far! keep it up!")            
