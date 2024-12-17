#Learnig about the FILTER FUNCTION: 

#Code without the Filter function
a = []
def filter_all(string):
    for i in string:
        if len(i) > 4:
            a.append(i)

list_of_words = ['shaheer', "city", 'abc', 'a', 'karachi']
filter_all(list_of_words)
print(a)

#Code with the Filter Function

def filtered_words(string):
    return len(string) > 4

ls = ['Shaheer', "Jamal", "Karachi", 'city', 'abc']
# filtered = filter(filtered_words, ls) #This and the below line of lambda functions gonna do the same thing
filtered = filter(lambda xyz: len(xyz) > 4 , ls)

# print(filtered) 
print(list(filtered))

