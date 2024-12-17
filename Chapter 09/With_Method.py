with open("Chapter 09\MySelf.txt", "w") as self_intro:
    self_intro.write("My name is Shaheer Jamal and I am a Python programmer.")
    
# with open("Chapter 09\MySelf.txt") as self_intro:
#     print(self_intro.read())


with open("Chapter 09\MySelf.txt", "a") as self_intro:
    self_intro.write("\nIm a 18 y/o guy from Karachi and Im very passionate about Py Programming")

with open("Chapter 09\MySelf.txt") as self_intro:
    print(self_intro.read())