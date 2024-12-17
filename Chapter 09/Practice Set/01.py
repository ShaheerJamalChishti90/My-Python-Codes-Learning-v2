# 1. Write a program to read the text from a given file ‘poems.txt’ and find out 
# whether it contains the word ‘twinkle’

with open("Chapter 09\poem.txt", "x") as poem:
    poem.write("Twinkle twinkle little star.\nHow I wonder what you are?.")

    
with open("Chapter 09\poem.txt") as poem:
    text = poem.read()
    
    if "Twinkle" in text:
        print("Twinkle is there in your poem")
    else:
        print("Twinkle is not there in your poem")