# Write a python function to remove a given word from a list ad strip it at the same 
# time.

ls = ["shaheer", "jamal", "chishti", "pakistan"]
print(ls)

rem = input("Which word would you like to remove: ").lower()

def removing():
    if rem in ls:
        ls.remove(rem)     
        print(f"The word {rem} is removed from the list: {ls}")   
    else:
        print('Invalid Entry')

removing()


ls02 = ["##Shaheer", "Jamal", "Chishti"]
str01 = "###shaheerjamalchishti###"

# print(ls02.strip("#"))
# print(str01.lstrip("#"))
# print(str01.rstrip("#"))

# print(type(str(ls02)))
