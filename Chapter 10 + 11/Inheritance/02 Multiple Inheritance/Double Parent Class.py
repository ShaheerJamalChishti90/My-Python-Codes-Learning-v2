# class Animal:
#     def __init__(self, species):
#         self.species = species

#     def make_sound(self):
#         return "Generic animal sound"

# class Pet:
#     def __init__(self, name):
#         self.name = name
        
#     def play(self):
#         return "Playing with pet"
    

# class Dog(Animal, Pet):
#     def __init__(self, name, species):
#         super().__init__(species)
#         Pet.__init__(self, name)
           
#     def Fetch(self):
#         return f'{self.name} is fetching the ball, {self.name}s breed is {self.species}'

# kutta = Dog('Kallu', 'Cane Corso')
# print(kutta.Fetch())

#BlackBox Ai Corrected Code: 

# Parent class Animal
class Animal: #Parent Class 01
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        return "Some generic sound"

# Parent class Pet
class Pet: #Parent Class 02
    def __init__(self, name):
        self.name = name

    def play(self):
        return f"{self.name} is playing."

# Child class Dog that inherits from both Animal and Pet
class Dog(Animal, Pet): 
    def __init__(self, name): #Yahan hum self parameter isliye de rahay hain takay jab hum object banayen tab hum har object ko specific dog name desakein agar aaisa nahi kia aurr hardcoded dog name buddy rakhdiya tou har object ko dog ka naam buddy milega
        # Initialize both parent classes
        super().__init__(species="Dog") #Hardcoded Animal Specie
        Pet.__init__(self, name)
 
    def make_sound(self):
        return "Bark"

    def fetch(self):
        return f"{self.name} is fetching a ball."

# Instantiate an object of the Dog class
my_dog = Dog(name="Buddy")

# Demonstrate the use of all inherited and overridden methods
print(f"Dog's name is {my_dog.name}.")
print(f"{my_dog.name} is a {my_dog.species}.")
print(f"{my_dog.name} says: {my_dog.make_sound()}")
print(my_dog.play())
print(my_dog.fetch())