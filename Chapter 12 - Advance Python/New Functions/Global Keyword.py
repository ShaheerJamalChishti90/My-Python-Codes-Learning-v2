#Global Keyword basically changes the global variable value inside a function
#If we don't use global keyword then the global variable value will not change

a = 45 #Global Variable

def func():
    global a
    a = 12 #Local Variable
    print(a)
    
func()
print(a)