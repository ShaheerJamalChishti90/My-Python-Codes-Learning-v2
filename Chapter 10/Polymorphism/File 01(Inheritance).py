# TWO WAYS TO ACHIEVE POLYMORPHISM
#1. Inheritance = An object could be treated of the same type as a parent class
#2. "Duck typing" = Object must have necessary attributes/methods



# from abc import ABC, abstractmethod

class Shape:   #Polymorphism starts from here, this is a single class named SHAPE having its own AREA method
    # @abstractmethod
    def area(self):
        pass

class Circle(Shape):    #when it comes to another class, it have the same method as the parent class but the way of working of that method is different
    def __init__(self, radius):
        self.radius = radius

    def area(self):  #Here you can see the way of working of AREA method is different
        return 3.14 * self.radius ** 2

class Square(Shape): #similarly, for this class to, the way of working is different here as well
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape): #and same for this and for the rest classes, the way of working is different
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 1/2 * self.base * self.height
    
class Cake(Circle):
    def __init__(self, radius, topping):
        super().__init__(radius)
        self.topping = topping
        

shapes = [Circle(4), Square(5), Triangle(6, 8), Cake(6, "berries")]

for i in shapes:
    print(f'{i.area()} cm**2')