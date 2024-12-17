# # SOME IMPORTANT SETS METHODS, RESPONSE BY CHAT-GPT:
# # https://chatgpt.com/share/9c3fbdc3-1894-4f4d-bca9-a0802d0a82b4


# e_set = set() # this is an empty set!

# # Set is a collection of non-repetitive elements.
# # sets mein value repeat nahi hoti!
# set0 = {0, 0, 2, 1, 2, 'shaheer', 0.123}
# set01 = {657484215966546549846163241654,5846, 5, 582, 1000}
# print(type(set01))

# # set0.add(3, 4, 5)

# print(set01.add(78945612300000000000000000000000000000000), type(set01))
# print(set01)

# # Sets Methods: (GPT Response)

# # Creating a set
# my_set = {1, 2, 3}

# # Adding an element
# my_set.add(4)
# print(my_set)  # Output: {1, 2, 3, 4}

# # Removing an element
# my_set.remove(2)
# print(my_set)  # Output: {1, 3, 4}

# # Removing an element that may or may not be present
# my_set.discard(5)  # No error even if 5 is not in the set
# print(my_set)  # Output: {1, 3, 4}

# # Clearing the entire set
# my_set.clear()
# print(my_set)  # Output: set()



s1 = {1 ,2 ,3}
s2 = {1, 2, 3, 4, 5}

abc = s1.intersection(s2)
print(abc) 


print(s1.difference(s2))