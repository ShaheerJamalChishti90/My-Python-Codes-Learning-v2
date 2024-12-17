# Dictionary is a collection of keys-value pairs.

# SOME IMPORTANT DICTIONAY METHODS, RESPONSE BY CHAT-GPT:
# https://chatgpt.com/share/9c3fbdc3-1894-4f4d-bca9-a0802d0a82b4


dic01 = {} # empty dictionary!!

dic = {
    "name":"ayesha",
    "age":"19",
    "city":"Karachi",
}

# print(dic)
# print(f"{dic['name'].capitalize()} is from {dic['city'].capitalize()} and they are approximately {dic['age']} years old! Shaheer is totally in love with em!!")

# print(type(dic))

# There are some Dict methods...

print(dic.items())
print(dic.keys())
print(dic.values())
print(dic.get("name"))
dic.update({"name":"snowie"})
print(dic)

my_dict = {'name': 'Alice', 'age': 25}

age = my_dict.pop('age') #Removes the specified key and returns its value. If the key is not found, the default value is returned.
print(age)  # Output: 25
print(my_dict)  # Output: {'name': 'Alice'}


item = my_dict.popitem() #Removes and returns the last key-value pair as a tuple

print(item) # Output: ("age", 25) 
print(my_dict) # Output: {'name': "Alice"}
