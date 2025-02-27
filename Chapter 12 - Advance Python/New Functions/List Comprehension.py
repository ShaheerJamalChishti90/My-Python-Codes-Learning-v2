ls = [2, 4, 6, 8, 10]

# new_ls = []
# for i in ls:
#     new_ls.append(i ** 2)
# print(new_ls)



# [new_list for iterator in obejct condition]
# [new_list for i in ls if i > 5 and i % 2]

new_ls = [item**2 for item in ls if item > 5 and item < 10]
print(new_ls)
