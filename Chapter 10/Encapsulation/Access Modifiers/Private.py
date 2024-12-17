name = input("Enter your name: ")
age = int(input("Enter your age: "))

class Person:   #Base Class 
    def __init__(self, name, age): #Attributes of the class
        self.__name = name #Private Attribute
        self.__age = age #Private Attribute
        
    def display_info(self):  #Public Method
        print(f"My name is {self.__name} and I am {self.__age} years old")

shaheer = Person(name, age)
shaheer.display_info()