import random

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?0123456789'
length = int(input('Enter password length: '))
password = ""

for i in range(length):
    password += random.choice(characters) #password = password + random.choice(characters)

# if length >= 8:    
#     print(f"Strong password: {password}")
# elif length <= 6 and length >= 4:
#     print(f"Medium password: {password}")
# else:
#     print(f"Weak password: {password}")
    
if n := len(password) >= 8:
    print(f"Strong password: {password}")
elif 4 <= n < 8:
    print(f"Medium password: {password}")
else:
    print(f"Weak password: {password}")
    
#If user wanna save the password in a file
def save_password():
    permission = input("Do you want to save the password in a file? (y/n): ")
    if permission.lower() == 'y':
        with open('password.txt', 'a') as f:
            f.write(f"{password}\n")
            print("Password saved successfully in password.txt file.")
    else:
        print("Password not saved.")

save_password()