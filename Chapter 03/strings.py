# mujhe strigns ke baray mein pata hai...

# strings are immutable..(mein inko bananay ke baad change nahi karsakta)

# mein apni grip strings slicing ke upper bana raha hoon
a = "Shaheer Jamal"
print("The length of a is",len(a))
print(f"Doing string slicing here, Mein tou {a[0:1] + a[3:7] + a[10:]} khaounga")

# doing string slicing [0,1,2,3] <== these are called index (BELOW CODE IS COPIED FROM REPLIT, MY PREVIOUS LECTURE/LEARNING)

# word = "amazingxyz"
# abc = word[1: : 2] # "mzn"
# print(abc)

name = "Shaheer Jamal Chishti"
print(len(name))

# print(name[ :-4])  # yahan ye -4 karne se name kii length  mein 4 se minus karke answer dega

# print(name[-7: ])  # yahan ye -5 index se start karega aurr end tak jayega....

# print(f'The total length of {name} is {len(name)} and if we minus 5 from the length, then it will be {[:-5]}')

# print(name[0], name[1], name[2], name[3], name[4], name[5], name[6],)

# print(f"I would like to eat {name[0]+name[3:7]+name[10:13]}")

# print(f"My name is {name[0:7]} and I am {len(name)} years old")

# "Shaheer Jamal Chishti"
# Doing negative slicing here
print(f"My name is {name[0:13]}, My roots are from {name[-7:-1]} and I am {len(name)-3} years old")


# dekho bhai:

# name = "Shaheer Jamal"
# slic = name[ :-5]
# slic = name[-5: ]

# agar hum name[:-5] karein, tou iska ye matlab hai ke ye name ki total length mein se 5 ko minus karega phir ans dega,
# aurr ye bhi kehsakty hain ke -5 index pe jo character hai ye srif wahin tak hii print karwayega kyun ke jaisa ke humein pata hai ke semicolin ke baad wala ending point hota hai issliye ye end wahan karwayega...


# aurr agar hum name[-5:] karein, tou iska ye matlab hai ke ye -5 index pe jo character hai wahan se shuru karega aurr end tak jayega,kyun ke semicolin se pehle wala starting point hota hai issliye ye starting wahan karwayega...




# f = "harie"
# print(f[-4:-2])

# fruit = "mango                      shaheer"
# print(len(fruit)) # yahan fruit ki length "34" hai, ab agar mein chahta hoon mein mere paas bas "mango shaheer" print ho tou mein yahan negative slicing karounga wo kaisy neechy dekho uske liye 

# print(fruit[-34:-28] , fruit[-7:-1])   


# haan tou bhai maine yahan kia kiyaa ke:

# 01: maine total length mein se 34 minus karwadiya jiska ans "0" aaya aurr "0" index pe mere paas "mango" ka "m" tha....
# 02: uske baad mein ne 34 mein se 28 ko minus karwadiya jiska ans "6" aaya aurr "6" index pe mere paas "mango" complete ho raha tha....

# 03: uske baad mein ne 34 mein se 7 ko minus karwadiya jiska ans 27 aaya aurr "27" index pe mere paas "shaheer" ka "s" tha...."
# 04: uske baad mein ne 34 mein se 1 ko minus karwadiya jiska ans 33 aaya aurr "33" index pe mere paas "shaheer" ka "r" tha lekin humein pata hai ke last walay index pe jo bhi alphabet hota hai wo neglect hojata hai iss wajha se "r" print nahi hoga..."

# a = "mango"
# print(a[0:4])

# end wala index number neglect hojata hai

# jaisay "mango" ismein total [0:4] hain ab agar mein isko print karwaounga tou  "mang" print hoga kyun ke end wala index number count nahi hota ignore hojata hai

# negative slicing
# neg slicing mein ye hota hai ki string ki length mein se apke index ka number minus hojata hai jaisy "mango" hai iski len 5 hai, ab agar [-4:-2] karounga ismein tou 5-4=1 aurr 5-2=3 tou 1:3 print hoga matlab index 1 pe jo alphabet hoga wo,LEKIN index 3 pe jo alphabet hoga wo print nahi hoga wo neglect hojayega aurr uski jaggha index 2 wala print hoga "an"

# a = "mango"
# print(a[-4:-2])

# print(a[0:-4])
# 5 - 4 = 1 "a[0:1]" and as we know that last wali value neglect hojati hai aurr ussay pehly wali aati hai so the ans will be "m"




# a = input("Name: "), int(input("Age: ")), float(input("Height: ")) #YE MUJHE ANSWER DERAHA HAI AS A TUPLE
a = f"{input("Name: ")} \n{int(input("Age: "))} \n{float(input("Height: "))}" #YE MUJHE ANSWER NORMALLY DERAHA HAI 

print(a)