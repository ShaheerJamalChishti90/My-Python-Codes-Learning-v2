name = input("Enter your name: ")
age = int(input("Enter your age: "))

class Person:   #Base Class 
    def __init__(self, name, age): #Attributes of the class
        self._name = name #Protected Attribute
        self._age = age #Protected Attribute
        
    def display_info(self):  #Public Method
        print(f"My name is {self._name} and I am {self._age} years old")

shaheer = Person(name, age)
shaheer.display_info()
print(dir(shaheer))