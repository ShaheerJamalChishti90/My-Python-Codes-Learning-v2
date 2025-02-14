class Animal:
    def sleep(self):
        print("Animal can sleep")

    def eat(self):
        print("Animal can eat")


class Dog(Animal):
    def bark(self):
        print("Dog barks")
        

class Bulldog(Dog):
    def bark(self):
        print("Bulldog barks loudly")
        
class Canecorso(Dog):
    def power(self):
        print("Canecorso is more powerful")


class Cat(Animal):
    def meow(self):
        print("Cat meow")
        
        
# Create instances of each class
my_animal = Animal()
my_dog = Dog()
my_bulldog = Bulldog()
my_canecorso = Canecorso()
my_cat = Cat()

# Call methods
my_animal.sleep()           # Animal can sleep
my_animal.eat()            # Animal can eat

my_dog.bark()              # Dog barks
my_dog.eat()               # Animal can eat (inherited from Animal)

my_bulldog.bark()          # Bulldog barks loudly
my_bulldog.eat()           # Animal can eat (inherited from Animal)

my_canecorso.bark()        # Dog barks (inherited from Dog)
my_canecorso.power()       # Canecorso is more powerful

my_cat.meow()              # Cat meow