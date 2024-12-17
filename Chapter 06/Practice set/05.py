# Write a program which finds out whether a given number is present in a list or not

num_list = [1, 2, 3, 4, 5]

user_input  = int(input("Enter any number, 5 > number > 0: "))

if user_input in num_list:
    print(f"{user_input} is present in the list")
else:
    print(f"{user_input} is not present in the list")

# Write a program which finds out whether a given name is present in a list or not

user_names = ["shaheer", "jamal", "chishti"]

user_input = input("Enter your name here: ")

if user_input in user_names:
    print(f"your name \'{user_input}\' is in the list, you are selected ")
else:
    print(f"your name \'{user_input}\' is not in the list, you are not selected")