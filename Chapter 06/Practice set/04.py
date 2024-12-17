# Write a program to find whether a given username contains less than 10 
# characters or not.


user_name = input("Enter your name here: ")

if len(user_name) < 10:
    print(f'Your username has been updated, the new username is {user_name}')
else:
    print(f'Error: username length must be less than 10 characters, username length is {len(user_name)}')