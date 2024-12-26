# Write a simple class Car that has a
# private attribute _speed. Include methods to set and get the speed.

class Car:  #Simple class of Car
    def __init__(self):
        self._speed = 0   #Protected Attribute

    def get_speed(self):   #Method of Getting the speed of the Car
        return f"This is the speed of the car: {self._speed}"

    def set_speed(self, speed):   #Method of Setting the speed of the Car
        self._speed = speed
        

    my_car = property(get_speed, set_speed)

tesla = Car()
tesla.set_speed(120)
print(tesla.my_car)