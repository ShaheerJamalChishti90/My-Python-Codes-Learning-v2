a = ['Shaheer', 'Jamal', "Chishti"] 

def add_word(string): #This function and the Lambda function below is gonna do the same work
    return string + "'s" 

# mapping = map(len, a) #I can do some more things like this by using a map function 
# mapping = map(type, a)
# maping = map(lambda xyz: xyz +'a', a) #Its gonna add that particular word in string ('a') in the end of the string(in this case: the list a)
mapping = map(add_word, a)
print(list(mapping))
     