#"Duck typing" = Another way to achieve polymorphism besides Inheritance
#Object must have the minimum necessary attributes/methods
#"If it looks like a duck and quacks like a duck, it must be a duck."


class Animal:
    alive = True


class Cat(Animal):  #In this case cat is inheriting from animal, meeting the minimum requirments(methods)
    def speak(self):
        return "Meow"
    
class Dog(Animal): #same in this case, dog is meeting the minimum requirments of animal, it has the method speak and is inheriting from Animal
    def speak(self):
        return "Woof"
    
class Bike(Animal): #this method comes out of no where, so i make it inherit from Animal and set the method speak init so it can be count in the list of animals
    def speak(self):
        return "Beep Beep"
    
animal = [Cat(), Dog(), Bike()]
for a in animal:
    print(f"{a.speak()}, Is alive = {a.alive}")


    

