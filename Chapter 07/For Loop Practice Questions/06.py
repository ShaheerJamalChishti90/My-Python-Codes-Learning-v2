# Reverse a String: Write a program that reverses a string provided by the user using a for loop.


string = input('Enter anything here to reverse it: ')
r_str = ""

for i in string:
    if len(string)  < 2:
        print("Invalid Entry")
    else:
        r_str = i + r_str #hello
print(r_str)    