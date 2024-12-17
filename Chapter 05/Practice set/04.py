# Q4: What will be the length of following set s:

# s = set()
# s.add(20)
# s.add(20.0123)
# s.add('20') # length of s after these operations?
# s.add((4, 5, 6))

# print(len(s))

# s = {}
# s = set()
# s = ()
# s = [] 
# print(type(s))
# What is the type of 's'?


# Q4: Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assume that the names are unique.

dic = {}

name = input("Enter your name: ")
lang = input("Enter your preferred lang: ")
dic.update({name:lang})

name = input("Enter your name: ")
lang = input("Enter your preferred lang: ")
dic.update({name:lang})

name = input("Enter your name: ")
lang = input("Enter your preferred lang: ")
dic.update({name:lang})

print(dic)