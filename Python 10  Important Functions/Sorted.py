# ls = [1, 4, 6, 85, 9, 52]
# print(sorted(ls)) #By default its gonna sort the values in the ascending order 
# print(sorted(ls, reverse=True))  #By doing this i can print the values in the decending order

 
 
#Below is basically the list having dictionary inside it, dict have key value pairs of person name and age
#Im gonna print the person's info according to his age in the form of list
pr = [
    {"name": "John", "age": 30},
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 35},
    {"name": "Charlie", "age": 20}
]

sr1 = sorted(pr, key=lambda xyz: xyz['age']) #This gona gime the info in the default ascending order
sr2 = sorted(pr, key=lambda xyz: xyz['age'], reverse=True) #This gona gime the info in the reverse order
print(list(sr1)) 
print(list(sr2)) 