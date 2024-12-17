# Taking inputs for a list
n = int(input("Enter number of elements: "))
my_list = []

for i in range(n):
    element = input(f"Enter element {i+1}: ")
    my_list.append(element)

print("List:", my_list)

# my_list.append(n)
# print(my_list)  

# e_tup = ()
# user = input("name: ").capitalize()

# e_tup += (user,)

# print(e_tup)