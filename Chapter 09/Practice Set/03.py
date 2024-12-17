# Write a program to generate multiplication tables from 2 to 20 and write it to the 
# different files. Place these files in a folder for a 13 – year old.

# import os

# os.mkdir("D:\\Visual Studio Codes\\Learning Python 2024 v2\\Chapter 09\\Practice Set\\Tables Folder")

number = int(input("Enter any number here to print its table: "))

def  write_to_file():
    with open(f"D:\\Visual Studio Codes\\Learning Python 2024 v2\\Chapter 09\\Practice Set\\Tables Folder\\Table of {number}", "a") as file:
        file.write(f"Table of {number}\n\n")
        for i in range(1, 11):
            file.write(f'{number} x {i} = {number*i}\n')
            
    print(f"The table of {number} is printed to its designated file:")
write_to_file()