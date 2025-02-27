# 1. Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not
# present, a message without exiting the program must be printed prompting the same.
import os
username = input("Enter your name: ")

# with(
#         open("D:\Visual Studio Codes\Learning Python 2024 v2\Main Learning\Chapter 12 - Advance Python\\01- Practice Set\\one.txt", "r") as f1,
#         open("D:\Visual Studio Codes\Learning Python 2024 v2\Main Learning\Chapter 12 - Advance Python\\01- Practice Set\\two.txt", "r") as f2
#     ):
     

try: 
        f1 = open("D:\Visual Studio Codes\Learning Python 2024 v2\Main Learning\Chapter 12 - Advance Python\\01- Practice Set\\one.txt", "r") 
        f2 = open("D:\Visual Studio Codes\Learning Python 2024 v2\Main Learning\Chapter 12 - Advance Python\\01- Practice Set\\two.txt", "r") 

except FileNotFoundError as fe:
        print(f"Sorry {username}, the file {fe} does not exist. Please check the file name once again.")
        
else:
        print("These are your files:")
        print(f1.read())
        print(f2.read())
        # print(f3.read())
        
        f1.close()
        f2.close()
        

finally:
        print("Thanks for using our software.")
        