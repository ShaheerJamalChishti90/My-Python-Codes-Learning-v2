name = input("Enter your name: ")
age = int(input("Enter your age: "))

class Person:   #Base Class 
    def __init__(self, name, age): #Attributes of the class
        self.name = name #Public Attribute
        self.age = age #Public Attribute
        
    def display_info(self):  #Public Method
        print(f"My name is {self.name} and I am {self.age} years old")

shaheer = Person(name, age)
shaheer.display_info()
# print(dir(shaheer))