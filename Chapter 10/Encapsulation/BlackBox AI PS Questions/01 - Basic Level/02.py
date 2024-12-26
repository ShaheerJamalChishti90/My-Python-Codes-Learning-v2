class Car:
    def __init__(self):
        self.__speed = 0
        
    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value < 0:
            raise ValueError("Speed cannot be negative")
        elif value > 200:
            raise Warning('Value is too high, slow down!')
        else:
            self.__speed = value

Fortuner = Car()
Fortuner.speed = 100
print(Fortuner.speed)  