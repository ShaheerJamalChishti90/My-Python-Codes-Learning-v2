ls = [{"Name":"Shaheer",
       "Roll#": 17,
       "Marks":89},
      
      {"Name":"Dua",
        "Roll#": 32,
        "Marks": 94},
      
      {"Name":"Namirah",
       "Roll#":33,
       "Marks":98 
      }]


user_choice = int(input("Enter the roll here: "))

for i in ls:
    if user_choice == i["Roll#"]:
        ls.remove(i)
print(ls)
        