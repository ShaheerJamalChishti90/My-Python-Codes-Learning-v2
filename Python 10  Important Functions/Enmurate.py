tasks = ["write code", "attend meeting", "write report", "off"]

# for i in range(len(tasks)):
#     task = tasks[i]
#     print(f"{i+1}: {task}")
    
    
    
# for i, task in enumerate(tasks):
#     print(f"{i+1}: {task}")

# print(list(enumerate(tasks)))

marks = [48, 58, 78, 72, 85]

# index = 0
# for i in marks:
#     print(i)
#     if index == 3:
#         print("Shaheer scored this marks")
#     index += 1
    
    
for shaheer, i in enumerate(marks):
    print(i)
    if shaheer == 3:
        print("This guy shaheer scored this marks")

    
