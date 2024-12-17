tasks = ["write code", "attend meeting", "write report", "off"]

for i in range(len(tasks)):
    task = tasks[i]
    print(f"{i+1}: {task}")
    
    
    
for i, task in enumerate(tasks):
    print(f"{i+1}: {task}")

print(list(enumerate(tasks)))