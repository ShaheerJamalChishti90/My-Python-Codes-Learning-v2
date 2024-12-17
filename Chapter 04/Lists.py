# In simple terms LIST is a container which can store number of values of different data types!!
# One more thing to remember, LISTs are mutable(unlike strings, they can be change originally )


list_abc = ["Shaheer", 18, 5.95, True]
print(list_abc[0:2])

list_abc[0] = "Muhammad Shaheer Jamal Chishti" # I CHANGED THE WHOLE STRING OF LIST, THIS IS POSSIBLE HERE BC OF ITS MUTABILITY 


# Unlike Strings, The original value can be changed, yu can add, remove, and do many more things with a LIST.
# print(list_abc)

# Doing some List Slicing


# abc = ["Shaheer", "Mishkat", "Basit", 1100, 1.000, False, True]
# marks = float(input("Enter your marks here: "))

# if marks >= 990:
#     print(f"{abc[1]} scored {marks} in her SSC Part 2 out of {abc[3]}, many many congragulations to her!")
# else:
#     print(f"{abc[1]} socred {marks} in her SSC Part 2")




# Can i take input from the user and make the list of it?

abc1 = input('''Enter your details below;\nName: ''')

abc2 = int(input('''Enter your details below;\nAge: '''))

abc3 = int(float(input('''Enter your details below;\nHeight: ''')))

a = [abc1, abc2, abc3]

print(a)

