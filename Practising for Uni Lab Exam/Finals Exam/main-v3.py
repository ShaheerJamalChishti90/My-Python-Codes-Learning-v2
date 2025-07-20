try:
    x = int(input("X here: "))
    y = int(input("Y here: "))

    division = x / y

except ValueError:
    print("Dear, you cant enter the non-integer value")

except ZeroDivisionError:
    print("Dear, you cant divide the value by 0!")

except SyntaxError:
    print("Dear, There's any syntax error in there")

else:
    print(f"The division of {x} and {y} is {int(division)}")

finally:
    print("There we go the code is finally completed!")