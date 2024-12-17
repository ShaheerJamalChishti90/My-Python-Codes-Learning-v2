# Write a program to greet all the person names stored in a list ‘l’ and which starts 
# with S.

l = ["Harry", "musa", "achin", "Rahul"]

for i in l:
    if i.startswith('S'):
        print("Hello, " + i)  # prints "Hello, Soham" and "
        break
    else:
        print("name isnt there in the list")
    break



# My code: taking input name from the user, storing it into list, then checking the condition:

name = input("name: ").capitalize()
list01= []
list01.append(name)

# print(list01) # Do not uncomment this line!

for x in list01:
    if x.startswith('S'):
        print(f'=>\n=> Hellow Mr/Ms {x}, Hope you are having a great day.')  # prints "Hello, Soham" 
    else:
        print("your name isnt stored in the list")