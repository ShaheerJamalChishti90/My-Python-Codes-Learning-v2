# Modify the Car class to use properties for
# getting and setting the speed instead of direct access to the private attribute.

class Car:
    def __init__(self):
        self.__speed = 0
        
        
    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def set_speed(self, value):
        if value < 0:
            raise ValueError("Speed cannot be negative")
        elif value > 200:
            raise Warning('Value is too high, slow down!')
        else:
            self.__speed = value

    def accelerate(self):
        self.__speed += 10   #self.__speed = self.__speed + 10

    def brake(self): 
        self.__speed -= 10  #self.__speed = self.__speed - 10



Fortuner = Car()
Fortuner.set_speed = int(input("Enter the speed: "))

if Fortuner.set_speed < 0:
    print("C'mon man, accelerate it!")
    Fortuner.accelerate()

elif Fortuner.set_speed > 200:
    print("Slow down!")
    Fortuner.brake()

elif Fortuner.set_speed > 250:
    print("You're going too fast!")


else:
    print(f"Speed = {Fortuner.speed}")


