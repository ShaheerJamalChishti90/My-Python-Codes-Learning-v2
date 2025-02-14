#Without using Walrus Operator
# c = input("Enter your country here: ")

# n = len(c)
# if n > 8:
#     raise Exception ("Country's name is too long!")
# elif n <= 8:    
#     print(f"Country's name: {c}\ncountry's length: {n}")
# else:
#     raise ValueError

#Using Walrus Operator
c = input("Enter your country here: ")

if (n := len(c)) <= 8:
    print(f"Country's name: {c}\ncountry's length: {n}")
elif (n := len(c)) > 8:
    raise Exception ("Country's name is too long!")
else:
    raise ValueError