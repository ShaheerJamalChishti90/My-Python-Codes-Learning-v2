# Heres the link of most used STRINGS FUNCTIONS in python
# https://chatgpt.com/share/1e047084-ebe3-48bd-9c71-62d2e04136de

a = "shaheer jamal chishti"

print(len(a))

print(a.endswith("chishti"))
print(a.startswith("shaheer"))

print(a.count('a'))

print(a.capitalize())

print(a.isdecimal())

print(a.find("j"))

a01 = a.center(50)
print(len(a01))
print((a.center(50, "-")))

abc = "hello world".split()
print(abc)
# Output: ["hello", "world"]

aa = ["Karachi", 'Lahore', 'Islamabad']
print(" - ".join(aa))

bb = 'Shaheer is a good boy, Shaheer is from Karachi, Shaheer is 18y/o, Shaheer wanna study in Germany aka Deutschland'
print(bb.replace("Shaheer", "Shaheer Jamal Chishti"))

print(a.title())

print(a.index("chishti"))


full_name = a.replace("shaheer", "Muhammad shaheer")
print(full_name.title())