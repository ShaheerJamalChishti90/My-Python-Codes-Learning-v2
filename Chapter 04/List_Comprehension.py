# NEW_LIST = [NEW_ITEM FOR ITEM IN LIST]

# NEW_ITEM: The ITEM with the calculation on it.
# (Yahan humari calculations hongi, jo bhi calcuate karwana hai jo bhi print karwana hai wo yahan karwaeingy)

# ITEM: Item(it can be anything)

# LIST: Basically the list

# NEW_LIST = [NEW_ITEM FOR ITEM IN LIST IF CONDITION]


ls = ['shaheer', 'jamal', 'chishti']
a_ls = []

nw_ls = [a_ls.append(item) for item in ls if "a" in item]
print(f"{a_ls}\n Theres something special in this list!!")