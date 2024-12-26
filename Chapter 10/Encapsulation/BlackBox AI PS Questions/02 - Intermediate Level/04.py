# Create a base class Animal with a private attribute _species. Then create a derived class Dog that tries to access the _species attribute. What happens? Explain why.
# Encapsulation in a Real-World Scenario


# class Animal:
#     def __init__(self, species):
#         self.__species = species

# class Dog(Animal):
#     def __init__(self, species):
#         Animal.__init__(self, species)
#         print(self.__species)  

# buddy = Dog('Cane Corso')
# print(buddy.__species)   
    
class Animal:
    def __init__(self, species):
        self.__species = species

    def get_species(self):
        return self.__species  # Provide a public method to access the private attribute

class Dog(Animal):
    def __init__(self, species):
        Animal.__init__(self, species)
        print(self.get_species())  # Use the public method to access the species

buddy = Dog('Cane Corso')
# Access the species using the public method
    

