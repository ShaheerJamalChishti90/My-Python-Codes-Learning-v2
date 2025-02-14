#Walrus Operator
# it can assign and use the value at the same time

name = input("Enter your name here: ")

# if len(name) > 8:
#     raise ValueError("Your name length is too long!")
# elif len(name) == 0:
#     raise ValueError("Name length cant be zero!")
# else:
#     print(f"Your name is updated: {name}")
    
    
if (n := len(name)) > 8:
    raise ValueError(f"Your name length is too long!, expected <= 8, got {n}")
print(f'Name: {name}')

# if (n := len([1, 2, 3, 4, 5])) > 3:
#     print(f"List is too long ({n} elements, expected <= 3)")