# Repeat program 4 for a list of such words to be censored.

# List of words to censor
censor_words = ["donkey", "horse", "cow", "donkey", "cat"]  # Add more words to censor

# Open the file and read its contents
with open("D:\\Visual Studio Codes\\Learning Python 2024 v2\\Chapter 09\\Practice Set\\nm_ls.txt", "r") as file:
    content = file.read()

# Replace each word from the list with '#####'
for word in censor_words:
    if word == 'donkey':
        content = content.replace(word, "#####")
        
        
# new_list = [content.replace(word, "###") for word in censor_words if word == "donkey"]

# Write the updated content back to the same file
with open("D:\\Visual Studio Codes\\Learning Python 2024 v2\\Chapter 09\\Practice Set\\nm_ls.txt", "w") as file:
    file.write(str(content))
    # file.write("\nWords have been censored successfully!")

# print("Words have been censored successfully!")





