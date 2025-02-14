# Inheritance and Protected Attributes:
# Create a base class Animal with a protected attribute _type.
# Create a subclass Dog that modifies _type and adds its own methods.

class Animal:
    def __init__(self):
        self._type = "Animal"

class Dog(Animal): 
    def __init__(self):
        super().__init__()
        self._type = "Animal: Dog"
        
    def breed(self):
        print("Golden Retriever")

shaheers_dog = Dog()
shaheers_dog.breed()

        