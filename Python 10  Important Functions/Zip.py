names  = ['David', 'John', 'James', 'Sarah']  
ages = [23, 34, 45, 90]  
genders = ['Male', 'Male', 'Male', 'Female']

# for i in range(min(len(names), len(ages))):
#     name = names[i]
#     age = ages[i]
#     print(f"{name} is {age} years old")


combined = list(zip(names, ages, genders))
# print(combined)

for name, age, gender in combined:
    print(f"{gender}: {name} is {age} years old")
