try:
    a = int(input("Enter the numerator here: "))
    b = int(input("Enter the denomerator here: "))
    result = a/b

except ZeroDivisionError as e:
    print(e)
    print('Ooops! In math you dont divide anything with ZERO! Thats inappropriate')

except ValueError as e:
    print(e)
    print('Are you idiot or what? Enter the fucking correct integer there')

except Exception as e:
    print(e)
    print("Invalid Input! we dont support such type of shit in this program")

else:
    print(result)
    
finally:
    print('This comes in the finally block so it always gonna print')
